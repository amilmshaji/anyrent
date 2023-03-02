from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

from accounts.models import Account
from .models import Message

class ChatView(View):
    def get(self, request):
        users = Account.objects.exclude(id=request.user.id)
        return render(request, 'chat/chat.html', {'users': users})

    def post(self, request):
        sender = request.user
        receiver_id = request.POST.get('receiver')
        receiver = Account.objects.get(id=receiver_id)
        message = request.POST.get('message')
        Message.objects.create(sender=sender, receiver=receiver, message=message)
        return render(request, 'chat/chat.html', {'receiver': receiver})
