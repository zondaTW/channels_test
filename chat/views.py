import json

from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def api_room(request, room_name):
    room_group_name = f'chat_{room_name}'
    layer = get_channel_layer()
    async_to_sync(layer.group_send)(room_group_name, {
           'type': 'chat_message',
           'message': f"Hello World: {room_group_name}"
        })
    return HttpResponse(f"Hello World: {room_group_name}")