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

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

     
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

     
    def put(self, request, id):
        order = self.get_object()
        serializer = self.serializer_class(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     
    def delete(self, request, id):
        order = self.get_object()
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class UpdateOrderStatusView(generics.UpdateAPIView):
    serializer_class = OrderStatusUpdateSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

     
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

