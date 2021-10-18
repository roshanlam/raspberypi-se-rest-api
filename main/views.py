from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime

from utils import is_json
from models import website

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def index(request):
    data = {
        "Message ": "Hello",
        "Date ": datetime.now()
    }
    print(is_json(data))
    return JsonResponse(data)

class WebsiteList(APIView):
    def get(self, request):
        websiteOne = website.objects.all()
        serializer = WebsiteSerializer(websiteOne, many = True)
        return Response(serializer.data)

    def post(self):
        pass