from rest_framework import status
from .exceptions import CustomAPIException
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
  message = None

  if isinstance(exc, CustomAPIException):
    if exc.is_str:
      message = str(exc)
    else:
      message = exc.detail
  else:
    message = str(exc)

  if exc:
    if isinstance(exc, APIException):
      return Response(data={
        "error": True,
        "message": message
      }, status=(exc.get_codes() if isinstance(exc.get_codes(), int) else status.HTTP_500_INTERNAL_SERVER_ERROR))
    else:
      return Response(data={
        "error": True,
        "message": str(exc)
      }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  else:
    response = exception_handler(exc, context)
    return response
