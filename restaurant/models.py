from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    bookingdate = models.DateField()

    def __str__(self):
        return self.name + '@' + str(self.bookingdate)

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return self.get_item()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'