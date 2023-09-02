from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_menu_item(self):
        item = Menu.objects.create(title='Burger', price=10.00, inventory=10)
        self.assertIn(item.get_item(), ['Burger : 10.00', 'Burger : 10', 'Burger : 10.0'])