from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.
class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        response_data = {"message": "hello Auth"}
        return Response(data=response_data, status=status.HTTP_200_OK)