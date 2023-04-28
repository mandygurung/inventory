from django.urls import path
from apps.accounts import views

app_name = "accounts"

urlpatterns = [
    path("", views.LoginView.as_view(), name=""),
    path("authenticate/", views.LoginView.as_view(), name="authenticate"),
]