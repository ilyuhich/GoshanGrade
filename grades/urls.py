from django.urls import path
from grades.views import hello_message

urlpatterns = [
    path('', hello_message, name='main'),
]