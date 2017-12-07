from django.db import models
import django.contrib.auth.models as auth
from .helpers import RandomFileName
from uuid import uuid4


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
    merchandise = models.ForeignKey(Merchandise, on_delete=models.PROTECT)
    users = models.ManyToManyField("User", through = 'UserScore')
    random_int = models.UUIDField(default=uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name

    def check_end(self):
        if self.now_count >= self.total_count:
            return True

    def add_count(self, coins):
        if self.check_end(): return 0
        if (int(coins)+self.now_count) > self.total_count:
            coins_for_return = int(coins)+self.now_count-self.total_count
            coins -= coins_for_return
        else:
            coins_for_return = 0
        self.now_count += int(coins)
        self.check_end()
        return coins_for_return


class User(auth.AbstractUser):
    cash = models.PositiveIntegerField(default=0)
    active_lottery = models.ManyToManyField(Lottery, through='UserScore')
    avatar = models.ImageField(upload_to=RandomFileName("avatar"), blank=True, null=True, default='default/avatar.png')

    def __str__(self):
        return self.username

    def check_coins(self, coins):
        if self.cash < int(coins) or self.cash == 0:
            return False
        else:
            return True


class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET(value='Deleted'))
    lottery = models.ForeignKey(Lottery, on_delete=models.SET(value='Deleted'))
    score = models.IntegerField(default=0, null=True)

    class Meta:
        unique_together = ('user', 'lottery')


def add_user_into_lottery(user, lottery, coins):
    if not user.check_coins(coins) or coins == 0:
        return False # some exception here
    else:
        current_lottery= Lottery.objects.get(random_int=lottery)
        if current_lottery.check_end():
            return False
        user.cash -= int(coins)
        try:
           nw=UserScore.objects.get(user=user, lottery=current_lottery)
        except UserScore.DoesNotExist:
            nw = UserScore(user=user, lottery=current_lottery, score=coins)
        else:
            nw.score += coins
        return_coins = current_lottery.add_count(coins)
        if return_coins > 0:
            user.cash += return_coins
        user.save()
        nw.save()
        current_lottery.save()


# Create your models here.
