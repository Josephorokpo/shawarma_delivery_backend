from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import OrderCreationSerializer, OrderStatusUpdateSerializer, UserOrderSerializer
from .models import Order


User = get_user_model()

# Create your views here.

class OrderCreateListView(generics.ListCreateAPIView):
    serializer_class = OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    @swagger_auto_schema(
        operation_summary="List all orders",
        responses={200: OrderCreationSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

     
    @swagger_auto_schema(
        operation_summary="Create a new order",
        responses={201: OrderCreationSerializer()},
        request_body=OrderCreationSerializer
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

    @swagger_auto_schema(
        operation_summary="Retrieve an order by ID",
        responses={200: OrderCreationSerializer()}
    ) 
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update an order by ID",
        responses={200: OrderCreationSerializer(), 400: "Bad Request"},
        request_body=OrderCreationSerializer
    ) 
    def put(self, request, id):
        order = self.get_object()
        serializer = self.serializer_class(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete an order by ID",
        responses={204: "No Content"}
    ) 
    def delete(self, request, id):
        order = self.get_object()
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class UpdateOrderStatusView(generics.UpdateAPIView):
    serializer_class = OrderStatusUpdateSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

    @swagger_auto_schema(
        operation_summary="Update order status",
        operation_description="Update the status of an order. Only accessible by superusers.",
    ) 
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UserOrdersView(generics.ListAPIView):
    serializer_class = UserOrderSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="List all orders for a user",
        responses={200: UserOrderSerializer(many=True), 404: "Not Found"}
    ) 
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Order.objects.filter(customer__id=user_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"detail": "No orders found for this user."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserOrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderCreationSerializer
    permission_classes = [IsAuthenticated]

     
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        order_id = self.kwargs.get('order_id')
        return Order.objects.filter(customer__id=user_id, id=order_id)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        order = queryset.first()
        if not order:
            return Response({"detail": "Order not found for this user."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

