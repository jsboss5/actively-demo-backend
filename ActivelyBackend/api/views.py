import json
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . import validators

import sys
sys.path.insert(0, './workers')

def get_request_body_decoded(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    return body

# Create your views here.
class testView(APIView):
    def get(self, request, format=None):
        return Response({"hello world"})

class validColumns(APIView):
    def get(self, request, format=None):
        
        body = get_request_body_decoded(request)
        data = body["data"]
        valid_cols_list = validators.getValidColumns(data)

        return Response({"valid_cols": valid_cols_list})

