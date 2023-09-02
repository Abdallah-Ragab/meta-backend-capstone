from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse


class MenuViewTest (TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(title='Burger', price=10.00, inventory=10)
        self.menu2 = Menu.objects.create(title='Pizza', price=15.00, inventory=10)
        self.menu3 = Menu.objects.create(title='Pasta', price=20.00, inventory=10)

    def test_get_all(self):
        url = reverse('restaurant:menu')
        response = self.client.get(url)
        data = MenuSerializer(Menu.objects.all(), many=True).data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [{'id': 2, 'title': 'Burger', 'price': '10.00', 'inventory': 10}, {'id': 3, 'title': 'Pizza', 'price': '15.00', 'inventory': 10}, {'id': 4, 'title': 'Pasta', 'price': '20.00', 'inventory': 10}])