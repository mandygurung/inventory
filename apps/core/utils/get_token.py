from rest_framework_simplejwt.serializers import TokenRefreshSerializer


def get_access_from_refresh(refresh_token):
        data = {
            "refresh": refresh_token
        }
        serializers = TokenRefreshSerializer(data=data) #type: ignore

        serializers.is_valid(raise_exception=True)
        
        return serializers.data