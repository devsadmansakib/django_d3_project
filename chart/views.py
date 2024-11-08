from django.core.serializers import serialize
from django.http import JsonResponse
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SampleData
from .serializers import SampleDataSerializer
from .forms import SignUpForm

# ---------------------------------------
# Authentication Views
# ---------------------------------------


# View for user signup
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log in the user immediately after signup
            return redirect("dashboard")  # Redirect to the dashboard after signup
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


# View for user login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.success(request, "There was an error please try again...")
    return render(request, "login.html")


# View for user logout
def logout_view(request):
    logout(request)
    return redirect("login")  # Redirect to the login page after logout


# ---------------------------------------
# Web Views
# ---------------------------------------


# Dashboard view (requires login)
@login_required
def dashboard_view(request):
    return render(request, "dashboard.html")


# Chart view for displaying D3.js chart (requires login)
@login_required
def chart_view(request):
    data = SampleData.objects.all()
    # Convert data to JSON format for D3.js
    data_json = json.dumps([{"label": obj.label, "value": obj.value} for obj in data])
    return render(request, "chart.html", {"data": data_json})


# API documentation view (requires login)
@login_required
def api_documentation_view(request):
    return render(request, "api_documentation.html")


# ---------------------------------------
# API Views
# ---------------------------------------


# API view to get chart data (requires authentication)
class ChartDataAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = SampleData.objects.all()
        serializer = SampleDataSerializer(data, many=True)
        return Response(serializer.data)
