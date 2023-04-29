from django.shortcuts import redirect, render
from rest_framework.views import APIView
from apps.accounts.serializers import AuthenticationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.core.mixins import JWTTokenRequiredMixins
from django.conf import settings
# from datetime import datetime
import datetime
# Create your views here.
class LoginView(APIView):

    """
        API view that handles user authentication through a POST request.
    """
    serializer_class = AuthenticationSerializer

    def get(self, request):
        """
        If the request method is GET and there is no Authorization header in the request, the view
        renders a login form template with the page title "Login - StockHub" and the title "login".
        If there is an Authorization header or the request method is not GET, the view checks if there
        is a "next" query parameter in the request. If there is no "next" parameter, the view redirects
        the user to the "dashboard" endpoint of the "accounts" app. If there is a "next" parameter, the
        view redirects the user to that parameter.
        """

        if not request.headers.get("Authorization"):
            context = {
                "page_title": "Login - StockHub",
                "title": "login"
            }

            return render(request, "accounts/login.html", context=context)
        else:
            next = request.GET.get("next")
            if not next:
                return redirect("accounts:dashboard")
            else:
                return redirect(next)


    def post(self, request):
        """
        Validates the user's credentials using an instance of the AuthenticationSerializer.
        If the credentials are valid, the view returns a success response with a cookie that
        contains the user's access token. The cookie is set with the name and options specified in
        the Django project settings file. The cookie's expiration time is set to one minute after
        the current time.
        
        Returns:
            A success response with a cookie that contains the user's access token if the credentials
            are valid.
        """
         
        serializers = self.serializer_class(data=request.data)
        
        serializers.is_valid(raise_exception=True)

        response = Response(data={"msg": "Success"}, status=status.HTTP_200_OK)
        exp = datetime.datetime.now() + datetime.timedelta(minutes=1)
        ref_exp = datetime.datetime.now() + datetime.timedelta(minutes=10)

        str_exp = datetime.datetime.strftime(exp, "%d-%b-%Y %H:%M:%S")
        ref_str_exp = datetime.datetime.strftime(ref_exp, "%d-%b-%Y %H:%M:%S")

    
        response.set_cookie(
            key = settings.SIMPLE_JWT["AUTH_COOKIE"], 
            value = serializers.validated_data.get("access", None), 
            httponly = settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            expires = str_exp
        )

        response.set_cookie(
            key = "refresh_token",
            value = serializers.validated_data.get("refresh", None), 
            httponly = settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            expires = ref_str_exp
        )

        # response.set_cookie

        return response
    
    

class DashboardView(JWTTokenRequiredMixins, APIView):

    """
        View that renders dashboard page. It checks if the user is valid and 
        also is authenticated only then it returns the dashboard page. 
    """

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request):


        # html = render_to_string("index.html")

        # return Response(data={"html": html})

        return render(request, "index.html")

