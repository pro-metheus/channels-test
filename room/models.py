from django.db import models

# Create your models here.

from django.utils import timezone

class Room(models.Model):
    label=models.CharField(max_length=20)


class Message(models.Model):
    room=models.ForeignKey(Room)
    text=models.TextField()
    timestamp=models.DateTimeField(default=timezone.now())

    
