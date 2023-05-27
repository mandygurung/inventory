import re
from django.shortcuts import render
from apps.category.models import Category
from apps.core.mixins import JWTTokenRequiredMixins
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
# Create your views here.
class ProductView(JWTTokenRequiredMixins, ListAPIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    # serializer_class = 

    def get(self, request, *args, **kwargs):
        context = {
            "page_title": "Products - StockHub"
        }

        return render(request, "products/product.html", context=context)
    



class ProductCreateView(JWTTokenRequiredMixins, CreateAPIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request):

        categories = Category.objects.all()

        context = {
            "categories": categories,
            "page_title": "Create Product - StockHub"
        }

        return render(request, "products/create_product.html", context)
    


class ProductDetailView(JWTTokenRequiredMixins, UpdateAPIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]


    def get(self, request):

        context = {
            "page_title": "Detail Product - StockHub"
        }

        return render(request, "products/product_detail.html", context=context)