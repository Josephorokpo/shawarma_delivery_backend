
from .models import Order
from rest_framework import serializers


class OrderCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'size', 'status', 'quantity', 'created_at', 'updated_at']
        read_only_fields = ['id', 'customer', 'created_at', 'updated_at']
        
        
class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'size', 'status', 'quantity', 'created_at', 'updated_at']
        read_only_fields = ['id', 'customer', 'created_at', 'updated_at']
        
        
class UserOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'size', 'status', 'quantity', 'created_at', 'updated_at']