from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Grades


# Create your views here.
def hello_message(request):
    return HttpResponse("Hello from my soul, World!!!")


class AllGrades(ListView):
    model = Grades
    context_object_name = 'grades_list'
    ordering = ['grade_date']
