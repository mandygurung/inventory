from django.shortcuts import render
from apps.accounts import serializers
from apps.core.mixins import JWTTokenRequiredMixins
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from apps.category.serializers import CategorySerializer
from apps.category.models import Category

# Create your views here.
class CategoryView(JWTTokenRequiredMixins, ListAPIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    serializer_class = CategorySerializer

    queryset = Category.objects.all()

    def get(self, request):

        serializers = self.get_serializer(self.get_queryset(), many=True)

        context = {
            "page_title": "Category - StockHub",
            "categories": serializers.data
        }

        return render(request, "category/category.html", context=context)


class CategoryCreateView(JWTTokenRequiredMixins, CreateAPIView):


    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    serializer_class = CategorySerializer

    queryset = Category.objects.all()


    def get(self, request):

        context = {
            "page_title": "Create Category - StockHub"
        }

        return render(request, "category/create_category.html", context=context)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class CategoryDetailView(JWTTokenRequiredMixins, UpdateAPIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    serializer_class = CategorySerializer

    queryset = Category.objects.all()

    lookup_field = "id"

    def get(self, request, id):

        serializers = self.get_serializer(self.get_object())

        context = {
            "page_title": "Edit Category - StockHub",
            "category": serializers.data
        }

        return render(request, "category/edit_category.html", context=context)
    

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)