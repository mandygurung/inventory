from django.urls import path
from apps.supplier import views

app_name = "supplier"

urlpatterns=[
    path('', views.SupplierView.as_view(), name="supplier_view"),
    path('supplier-create/', views.SupplierCreateView.as_view(), name="supplier_create"),
    path('supplier-detail/<int:id>/', views.SupplierDetailView.as_view(), name="supplier_detail"),
]