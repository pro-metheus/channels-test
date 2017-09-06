from django.shortcuts import render

# Create your views here.
from .models import Message,Room


def chat(request,label):
    room,created=Room.objects.get_or_create(label=label)
    messages=reversed(Message.objects.filter(room=room).order_by("-timestamp")[:50])
    return render(request,'home.html',locals())
    
