from django.urls import reverse, resolve




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

        response = self.get_response(request)

        return response
    
        
    