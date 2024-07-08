from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import OrderSerializer, OrderStatusUpdateSerializer, UserOrderSerializer
from .models import Order

# Create your views here.

class OrderCreateListView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

     
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

