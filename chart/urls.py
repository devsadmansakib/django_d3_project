from django.urls import path
from .views import (
    login_view,
    chart_view,
    dashboard_view,
    logout_view,
    api_documentation_view,
    signup_view,
    ChartDataAPI,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# ---------------------------------------
# Web Routes
# ---------------------------------------

urlpatterns = [
    path("", login_view, name="login"),  # Default to login page
    path("dashboard/", dashboard_view, name="dashboard"),  # Dashboard/Home page
    path("login/", login_view, name="login"),  # Login page
    path("signup/", signup_view, name="signup"),  # Signup page
    path("chart/", chart_view, name="chart"),  # Chart page
    path("logout/", logout_view, name="logout"),  # Logout
    path(
        "api/docs/", api_documentation_view, name="api_documentation"
    ),  # API documentation
]

# ---------------------------------------
# API Routes
# ---------------------------------------

urlpatterns += [
    path(
        "api/chart-data/", ChartDataAPI.as_view(), name="chart-data-api"
    ),  # Chart data API
    path(
        "api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # JWT token obtain
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # JWT token refresh
]
