from django.db import models
import django.contrib.auth.models as auth
from .helpers import RandomFileName

class Merchandise(models.Model):
    name = models.CharField(default="", max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # цена, 999999 макс
    pic = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.name


# Нужно больше параметров


class Lottery(models.Model):
    name = models.CharField(default="", max_length=255)
    total_count = models.PositiveIntegerField(default=100, null=False)
    now_count = models.PositiveIntegerField(default=0)
    merchandise = models.ForeignKey(Merchandise)

    def __str__(self):
        return self.name


class User(auth.AbstractUser):
    cash = models.PositiveIntegerField(default=0)
    active_lottery = models.ManyToManyField(Lottery, through='UserScore')
    avatar = models.ImageField(upload_to=RandomFileName("avatar"), blank=True, null=True)
    def __str__(self):
        return self.username


class UserScore(models.Model):
    user = models.ForeignKey(User)
    lottery = models.ForeignKey(Lottery)
    score = models.IntegerField(default=0, null=True)


'''
class UserScore:
    user = models.ManyToManyField(User)
    lottery = models.ManyToManyField(Lottery)
    score = models.IntegerField(default=0, null=True)
    class Meta:
        unique_together = '''
# Create your models here.
