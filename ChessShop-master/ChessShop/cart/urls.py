from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('orders', views.OrderViewSet, basename='order')
#router.register('orderItems', views.OrderItemViewSet, basename='orderItem')
router.register('deliveryMethods', views.DeliveryMethodSerializer)

urlpatterns = [
    #path('api/products/', include('products.urls')),
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #path('api/users/', include('users.urls')),
    #path('api/main', include('main.urls')),
]
