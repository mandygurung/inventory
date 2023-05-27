from django.urls import path
from apps.product import views

app_name = "product"

urlpatterns = [
    path("", views.ProductView.as_view(), name="product-view"),
    path("product-create/", views.ProductCreateView.as_view(), name="product-create-view"),
    path("product-detail/", views.ProductDetailView.as_view(), name="product-detail-view"),
]