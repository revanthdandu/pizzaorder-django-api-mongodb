from django.db import models

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    PIZZA_TYPES_CHOICES = [
        ('Regular', 'Regular'),
        ('Square', 'Square'),
    ]

    PIZZA_SIZE_CHOICES = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]

    name = models.CharField(max_length=100)
    pizza_type = models.CharField(max_length=50, choices=PIZZA_TYPES_CHOICES, default='Regular')
    pizza_size = models.CharField(max_length=50, choices=PIZZA_SIZE_CHOICES, default='Small')
    pizza_toppings = models.ManyToManyField(Topping, related_name='pizza_list')

    def __str__(self):
        return self.name