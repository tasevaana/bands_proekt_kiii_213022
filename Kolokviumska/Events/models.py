from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    year = models.IntegerField()
    numOfEvents = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.country


class Event(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    poster = models.ImageField(upload_to='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isOpen = models.BooleanField()

    def __str__(self):
        return self.name + " " + self.date.__str__()


class EventBand(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.name + " " + self.band.name
