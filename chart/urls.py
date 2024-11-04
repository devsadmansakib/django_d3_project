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


urlpatterns = [
    path("", login_view, name="login"),
    path("dashboard/", dashboard_view, name="dashboard"),  # Home page
    path("login/", login_view, name="login"),
    path("chart/", chart_view, name="chart"),
    path("logout/", logout_view, name="logout"),  # Logout URL
    path("signup/", signup_view, name="signup"),
    path("api/docs/", api_documentation_view, name="api_documentation"),
    path("api/chart-data/", ChartDataAPI.as_view(), name="chart-data-api"),
]


urlpatterns += [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
