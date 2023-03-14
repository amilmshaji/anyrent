from django.urls import path

from chatbot import views

urlpatterns = [
    path('chatbot/', views.chatbot, name='chatbot'),

]
