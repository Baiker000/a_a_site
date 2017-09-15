from django.db import models
import django.contrib.auth.models as auth


class Merchandise(models.Model):
    name = models.CharField(default="", max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # цена, 999999 макс
    pic = models.ImageField(upload_to="images", blank=True, null=True)


# Нужно больше параметров


class Lottery(models.Model):
    name = models.CharField(default="", max_length=255)
    total_count = models.IntegerField(default=100, null=False)
    now_count = models.IntegerField(default=0)
    merchandise = models.ForeignKey(Merchandise)


class User(auth.User):
    cash = models.IntegerField(default=0)
    active_lottery = models.ManyToManyField(Lottery)

# Create your models here.
