from .utils import ip
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponseForbidden

class AllowOnlyCertainIPsMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

    # List of allowed IP addresses
    self.allowed_ips = ip.ALLOWED_IPS

  def __call__(self, request):
    server_ip = request.META.get('REMOTE_ADDR')
    client_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    
    print("Server IP:", server_ip)
    print("Client IP:", client_ip)

    if client_ip is not None and client_ip not in self.allowed_ips:
      return HttpResponseForbidden("You are not allowed to access this resource.")

    response = self.get_response(request)
    return response
