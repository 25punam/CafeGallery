from django.db import models

# Create your models here.

class CafeModel(models.Model):
    cafe_name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    img1 = models.ImageField(null=True, blank=True)
    img2 = models.ImageField(null=True, blank=True)
    img3 = models.ImageField(null=True, blank=True)
    img4 = models.ImageField(null=True, blank=True)
    opening_hours = models.CharField(max_length=40, null=True)
    opening_time =models.CharField(max_length=30, null=True)


class MenuModel(models.Model):
    YOUR_CHOICES = [
        ('Eat', ' Eat'),
        ('Drink', ' Drink'),
    ]
    cafe = models.ForeignKey(CafeModel, on_delete=models.CASCADE,  null=True)
    type = models.CharField(max_length=10, choices=YOUR_CHOICES)
    title = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=200)

