from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import User
from . import serializers

# Create your views here.
# class HelloAuthView(generics.GenericAPIView):
#     def get(self, request):
#         response_data = {"message": "hello Auth"}
#         return Response(data=response_data, status=status.HTTP_200_OK)
    

class UserCreateView(generics.GenericAPIView):
    serializer_class = serializers.UserCreationSerializer
    
    @swagger_auto_schema(
        operation_summary="Create a new user",
    )
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            response_data.pop('password', None)  # Ensure password is not included in the response
            return Response(data=response_data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)