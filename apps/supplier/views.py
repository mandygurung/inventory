from django.shortcuts import render
from apps.core.mixins import JWTTokenRequiredMixins
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.supplier.models import Supplier
from apps.supplier.serializers import SupplierSerializer

# Create your views here.
class SupplierView(JWTTokenRequiredMixins, ListAPIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    serializer_class = SupplierSerializer

    queryset = Supplier.objects.all()


    def get(self, request):

        serializer = self.get_serializer(self.get_queryset(), many=True)

        context = {
            "page_title": "Supplier - StockHub",
            "suppliers": serializer.data
        }

        return render(request, "supplier/supplier.html", context=context)
    

class SupplierCreateView(JWTTokenRequiredMixins, CreateAPIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    serializer_class = SupplierSerializer

    queryset = Supplier.objects.all()


    def get(self, request):

        context = {
            "page_title": "Create Supplier - StockHub",
        }

        return render(request, "supplier/create_supplier.html", context=context)
    
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SupplierDetailView(JWTTokenRequiredMixins, UpdateAPIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    serializer_class = SupplierSerializer

    queryset = Supplier.objects.all()

    lookup_field = "id"

    def get(self, request, id):

        serializer = self.get_serializer(self.get_object())

        context = {
            "page_title": "Update Supplier - StockHub",
            "supplier": serializer.data
        }

        return render(request, "supplier/edit_supplier.html", context=context)
    

    def put(self, request, *args, **kwargs):
        try:
            return super().put(request, *args, **kwargs)
        except Exception as e:
            print(e)