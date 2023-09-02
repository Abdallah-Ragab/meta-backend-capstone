from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer

# Create your views here.

def index(request):
    return render(request, 'helloworld.html')

class MenuItemView(ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    class Meta:
        model = Menu
        fields = '__all__'

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    class Meta:
        model = Menu
        fields = '__all__'


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]