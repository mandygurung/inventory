from django.shortcuts import render
from core.mixins import JWTTokenRequiredMixins
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
# Create your views here.
class ProductView(JWTTokenRequiredMixins, ListAPIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    # serializer_class = 

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


    