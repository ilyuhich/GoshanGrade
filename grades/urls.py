from django.urls import path
from .views import hello_message, AllGrades

urlpatterns = [
    path('', hello_message, name='main'),
    path('grades/', AllGrades.as_view(), name='all_grades'),
]