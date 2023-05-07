from django.db import models

# Create your models here.

class Booking(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    guese_number = models.IntegerField()
    comment = models.CharField(max_length=100)


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    menu_item_description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Person(models.Model): 
    name = models.CharField(max_length=20) 
    email = models.EmailField() 
    phone = models.CharField(max_length=20) 
