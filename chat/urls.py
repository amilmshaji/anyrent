from django.urls import path

from chat import views

urlpatterns = [
    path('chat/<int:recipient_id>/', views.chat_view, name='chat'),
    path('send_message/<int:recipient_id>/', views.send_message_view, name='send_message'),
]
