from django.urls import path
from apps.category import views

app_name = "category"

urlpatterns = [
    path('', views.CategoryView.as_view(), name="category_view"),
    path('category-create/', views.CategoryCreateView.as_view(), name="category_create"),
    path('category-detail/<int:id>/', views.CategoryDetailView.as_view(), name="category_detail"),
    path('export-to-excel/', views.CategoryExportToExcel.as_view(), name="export_to_csv")
]