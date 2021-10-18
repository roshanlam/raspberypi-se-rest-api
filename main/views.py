from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime

from utils import is_json

def index(request):
    data = {
        "Message ": "Hello",
        "Date ": datetime.now()
    }
    print(is_json(data))
    return JsonResponse(data)