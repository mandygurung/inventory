from django.urls import path
from apps.accounts import views

app_name = "accounts"

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("authenticate/", views.LoginView.as_view(), name="authenticate"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path('users/', views.UserView.as_view(), name="user_view"),
    path('create-users/', views.UserCreateView.as_view(), name="create_user"),
    path('detail-user/<int:id>', views.UserDetailView.as_view(), name="detail_user")
]