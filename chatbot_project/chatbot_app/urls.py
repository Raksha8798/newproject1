# chatbot_app/urls.py
from django.urls import path
from .views import Chatbot, home

urlpatterns = [
    path('', home, name='home'),
    path('chatbot/', Chatbot, name='chatbot'),
]
