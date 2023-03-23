from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Account, Message


@login_required(login_url='login')
def chat_view(request, recipient_id):
    recipient = get_object_or_404(Account, id=recipient_id)
    chatter = Account.objects.get(id=recipient_id)
    fname_value = chatter.fname
    lname_value = chatter.lname

    messages = Message.objects.filter(Q(sender=request.user, recipient=recipient) | Q(sender=recipient, recipient=request.user)).order_by('timestamp')
    current_user = request.user
    received_messages = Message.objects.filter(recipient=current_user).values('sender').annotate(
        latest_timestamp=Max('timestamp'))

    conversations = []
    for message in received_messages:
        latest_message = Message.objects.filter(recipient=current_user, sender=message['sender'],
                                                timestamp=message['latest_timestamp']).first()
        conversation = {
            'sender': latest_message.sender,
            'message': latest_message.message,
            'timestamp': latest_message.timestamp
        }
        conversations.append(conversation)
    # chatter=Message.objects.get(id=recipient_id)
    # print(chatter)
    context = {
        'recipient': recipient,
        'messages': messages,
        'conversations': conversations,
        'fname_value' : fname_value,
        'lname_value' : lname_value,

    }
    return render(request, 'chat/chat.html', context)

from django.db.models import Max

@login_required
def inbox(request):
    current_user = request.user
    received_messages = Message.objects.filter(recipient=current_user).values('sender').annotate(latest_timestamp=Max('timestamp'))

    conversations = []
    for message in received_messages:
        latest_message = Message.objects.filter(recipient=current_user, sender=message['sender'], timestamp=message['latest_timestamp']).first()
        conversation = {
            'sender': latest_message.sender,
            'message': latest_message.message,
            'timestamp': latest_message.timestamp
        }
        conversations.append(conversation)

    return render(request, 'chat/inbox.html', {'conversations': conversations})


@login_required(login_url='login')
def send_message_view(request, recipient_id):
    recipient = get_object_or_404(Account, id=recipient_id)
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            Message.objects.create(sender=request.user, recipient=recipient, message=message)
            return redirect('chat', recipient_id=recipient_id)
    context = {'recipient': recipient}
    return render(request, 'chat/send_message.html', context)




