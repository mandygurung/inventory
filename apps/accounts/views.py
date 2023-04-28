from django.shortcuts import render
from rest_framework.views import APIView
from apps.accounts.serializers import AuthenticationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class LoginView(APIView):

    serializer_class = AuthenticationSerializer

    def get(self, request):
        context = {
            "page_title": "Login - StockHub",
            "title": "login"
        }

        return render(request, "accounts/login.html", context=context)


    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        
        serializers.is_valid(raise_exception=True)

        response = Response(data={"msg": "Success"}, status=status.HTTP_200_OK)

        response.set_cookie("access_token", serializers.validated_data.get("access", None), httponly=True)

        return response
    
    





