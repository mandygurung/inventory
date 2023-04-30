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

    def dispatch(self, request, *args, **kwargs) :
        if not request.headers.get("Authorization") and not request.COOKIES.get("refresh_token"):
            return self.handle_no_permission()        
        response = super().dispatch(request, *args, **kwargs) # type: ignore

        return response
