import json
import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView

from rest_framework.response import Response

from .engine import validators, model_trainer
from .engine.database import Fake_Database

import sys
sys.path.insert(0, './workers')

# Create your views here.
class test_view(APIView):
    def get(self, request, format=None):
        return Response({"hello world"})

class valid_columns(APIView):
    def get(self, request, format=None):
        
        body = get_request_body_decoded(request)
        data = body["data"]
        valid_cols_list = validators.getValidColumns(data)

        return Response(
            {
                "valid_cols": valid_cols_list
            }
        )


class train_model(APIView):
    def post(self, request, format=None):
        body = get_request_body_decoded(request)
        print(body)
        pd_data = dictionary_to_pd(body['data'])
        inputs = body['inputs']
        output = body['output']

        #  I'm sorry I know this is bad but I cant be pressed to fix the circular import right now
        from .endpoints import global_database_instance
        model_id = model_trainer.train_and_store_model(pd_data, output, inputs, global_database_instance)

        return Response(
            {"model_id": model_id}
        )

# Helper Functions
def get_request_body_decoded(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    return body

def dictionary_to_pd(dic):
    return pd.DataFrame.from_dict(dic)
