from django.urls import reverse, resolve
from apps.core.utils.get_token import get_access_from_refresh
import datetime
from django.conf import settings

class JWTAuthentication:

    EXCLUDE = [
        "apps.accounts.views.LoginView",
    ]

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request, *args, **kwds):
        func_path = resolve(request.path)._func_path
        if "django.contrib.admin" not in func_path:
            if "access_token" in request.COOKIES and request.COOKIES.get('access_token') is not None:
 
                token = request.COOKIES.get('access_token')
                
                request.META["HTTP_AUTHORIZATION"] = f"Bearer {token}"
            
            elif "access_token" not in request.COOKIES \
                and "refresh_token" in request.COOKIES \
                and request.COOKIES.get('refresh_token'):
                
                tokens = get_access_from_refresh(request.COOKIES.get("refresh_token"))
            
                request.META["HTTP_AUTHORIZATION"] = f"Bearer {tokens.get('access')}"
                
                # response = super().dispatch(request, *args, **kwargs) #type: ignore

                response = self.get_response(request)
                
                exp = datetime.datetime.now() + datetime.timedelta(minutes=60)
                ref_exp = datetime.datetime.now() + datetime.timedelta(days=1)

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

        response = self.get_response(request)

        return response
    
        
    