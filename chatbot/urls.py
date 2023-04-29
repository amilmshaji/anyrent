from django.urls import path

from chatbot import views

urlpatterns = [
    path('chatbot/', views.chatbot, name='chatbot'),
    # path('chatbott/', views.chatbott, name='chatbott'),

]
