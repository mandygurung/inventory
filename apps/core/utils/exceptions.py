from rest_framework.views import exception_handler
from django.contrib import messages

def _exception_handler(exc, context):
    response = exception_handler(exc, context)

    error = {"error": {"status_code": 0, "details": {}}}

    if response is not None and response.data is not None:
        error["error"].update({
            "status_code": response.status_code,
        })
        for key, value in response.data.items():
            if isinstance(value, list):
                error["error"]["details"].update({
                    key: value[0]
                })
            else:
                error["error"]["details"].update({
                    key: value
                })
        
        response.data = error

    
    return response