from django.db import models

# Create your models here.
from django.db import models

from accounts.models import Account

from django.utils import timezone

class Message(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sent_messages',blank=True,null=True)
    recipient = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='received_messages',blank=True,null=True)
    message = models.TextField(blank=True,null=True)
    timestamp = models.DateTimeField(default=timezone.now)


