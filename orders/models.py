from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    SIZES = (
        ('SMALL', 'Small'),
        ('MEDIUM', 'Medium'),
        ('LARGE', 'Large'),
        ('EXTRA_LARGE', 'Extra Large'),
    )
  
    ORDER_STATUS = (
        ('PENDING', 'Pending'),
        ('IN_TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered'),
    )
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=30, choices=SIZES, default=SIZES[0][0])
    status = models.CharField(max_length=30, choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return f"<Order {self.size} by {self.customer.id}>"
