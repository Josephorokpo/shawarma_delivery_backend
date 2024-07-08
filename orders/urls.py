from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderCreateListView.as_view(), name='order_list_create'),
    path('<int:id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('<int:id>/status/', views.UpdateOrderStatusView.as_view(), name='order_status_update'),
    path('user/<int:user_id>/orders/', views.UserOrdersView.as_view(), name='user_orders'),
    path('user/<int:user_id>/orders/<int:order_id>/', views.UserOrderDetailView.as_view(), name='user_order_detail'),
]