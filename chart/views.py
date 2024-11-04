from django.core.serializers import serialize
from django.http import JsonResponse
import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SampleData
from .serializers import SampleDataSerializer
from .forms import SignUpForm


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log in the user immediately after signup
            return redirect(
                "dashboard"
            )  # Redirect to the dashboard or desired page after signup
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


# Web view for login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
    return render(request, "login.html")


@login_required
def dashboard_view(request):
    return render(request, "dashboard.html")


# Web view for rendering chart
@login_required
def chart_view(request):
    data = SampleData.objects.all()
    # Convert data to JSON format for D3.js
    data_json = json.dumps([{"label": obj.label, "value": obj.value} for obj in data])
    return render(request, "chart.html", {"data": data_json})


# API view to get chart data
class ChartDataAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = SampleData.objects.all()
        serializer = SampleDataSerializer(data, many=True)
        return Response(serializer.data)


def logout_view(request):
    logout(request)
    return redirect("login")  # Redirect to the login page after logout


@login_required
def api_documentation_view(request):
    return render(request, "api_documentation.html")
