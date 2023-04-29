from weakref import ref
from django.contrib.auth.mixins import AccessMixin
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from django.conf import settings
import datetime
# class ResponseMixin:

#     def set_cookies(self, response, **kwargs):
#         pass

#     def get_response(self, data, status_code, cookies=False):
#         response = Response(
#             data=data,
#             status=status_code
#         )

#         if cookies:
#             response = self.set_cookies(response)


class JWTTokenRequiredMixins(AccessMixin):


    def get_access_from_refresh(self, refresh_token):
        print("Getting refres")
        data = {
            "refresh": refresh_token
        }
        serializers = TokenRefreshSerializer(data=data) #type: ignore

        serializers.is_valid(raise_exception=True)
        
        return serializers.data

    def dispatch(self, request, *args, **kwargs) :
        if not request.headers.get("Authorization") and not request.COOKIES.get("refresh_token"):
            print("Has no ref and access")
            return self.handle_no_permission()
        elif not request.headers.get("Authorization") and request.COOKIES.get("refresh_token"):
            print("Has ref")
            tokens = self.get_access_from_refresh(request.COOKIES.get("refresh_token"))
            
            request.META["HTTP_AUTHORIZATION"] = f"Bearer {tokens.get('access')}"
            
            response = super().dispatch(request, *args, **kwargs) #type: ignore
            
            exp = datetime.datetime.now() + datetime.timedelta(minutes=1)
            ref_exp = datetime.datetime.now() + datetime.timedelta(minutes=10)

            str_exp = datetime.datetime.strftime(exp, "%d-%b-%Y %H:%M:%S")
            ref_str_exp = datetime.datetime.strftime(ref_exp, "%d-%b-%Y %H:%M:%S")
            
            response.set_cookie(
                key = "access_token",
                value = tokens.get('access'), 
                httponly = settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                expires = str_exp
            )

            response.set_cookie(
                key = "refresh_token",
                value = tokens.get('refresh'), 
                httponly = settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                expires = ref_str_exp
            )

            return response
        
        print("Has auth")
        response = super().dispatch(request, *args, **kwargs) # type: ignore
        print(response.status_code)
        print(dir(response))
        return response
