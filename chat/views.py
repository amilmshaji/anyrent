from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib.auth.models import User

from accounts.models import Account
from .models import Message

@login_required(login_url='login')
def chat_view(request, recipient_id):
    # if category_slug != None:


    recipient = get_object_or_404(Account, id=recipient_id)
    messages = Message.objects.filter(Q(sender=request.user, recipient=recipient) | Q(sender=recipient, recipient=request.user)).order_by('timestamp')
    context = {'recipient': recipient, 'messages': messages}
    return render(request, 'chat/index.html', context)


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



def all_list(request):
    current_user=request.user
    list=Message.objects.filter(
        Q(sender=current_user, recipient__isnull=False) | Q(sender__isnull=False, recipient=current_user)
    ).exclude(
        sender=current_user, recipient=current_user
    ).distinct()# This query uses the Q object to combine two conditions:
    # sender=current_user and recipient__isnull=False: This condition matches all messages sent by the current user to other users.
    # sender__isnull=False and recipient=current_user: This condition matches all messages received by the current user from other users.
    print(list)
    context = {
        'list': list
    }

    return render(request, 'chat/dummy.html',context)


