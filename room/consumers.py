from channels import Group
from channels.sessions import channel_session
from .models import Room,Message
import json

@channel_session
def ws_connect(message):
    prefix, label = message['path'].decode('ascii').strip('/').split('/')
    Group('chat-'+label).add(message.reply_channel)
    message.channel_session['room']=label


@channel_session
def ws_message(message):
    data=json.dumps(message['text'])
    Group('chat-'+label).send(data['text'])
    label=message.channel_session['room']
    room=Room.objects.get(label=label)
    message=Message(room=room,text=data['text'])
    message.save()

@channel_session
def ws_disconnect(message):
    Group('chat-'+message.channel_session['room'].discard(message.reply_channel))
