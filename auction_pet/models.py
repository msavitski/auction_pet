from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    balance = models.IntegerField(default=0)


class Pet(models.Model):
    PET_TYPES = [('cat', 'cat'), ('hedgehog', 'hedgehog')]
    pet_type = models.CharField(choices=PET_TYPES, max_length=2)
    kind = models.CharField(max_length=255)
    nick = models.CharField(max_length=255)
    owner = models.ForeignKey(User, models.CASCADE)


class Lot(models.Model):
    pet = models.ForeignKey(Pet, models.CASCADE)
    owner = models.ForeignKey(User, models.CASCADE, related_name='lots')
    start_price = models.IntegerField()
    finished = models.BooleanField(default=False)


class Bid(models.Model):
    value = models.IntegerField()
    owner = models.ForeignKey(User, models.CASCADE, related_name='bids')
    lot = models.ForeignKey(Lot, models.CASCADE, related_name='bids')
    accepted = models.BooleanField(default=False)
