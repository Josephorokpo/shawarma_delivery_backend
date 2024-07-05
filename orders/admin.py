from django.contrib import admin
from .models import Order

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ('size', 'status', 'quantity', 'created_at', 'updated_at')
  list_filter = ('created_at','size', 'status')
