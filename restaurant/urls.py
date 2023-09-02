from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import index
from .views import MenuItemView, SingleMenuItemView, BookingViewSet

router = DefaultRouter()
router.register(r'tables', BookingViewSet)

app_name = 'restaurant'

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='single_menu'),
    path('booking/', include(router.urls), name='booking'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
