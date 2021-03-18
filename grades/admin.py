from django.contrib import admin
from .models import Quarters, Subjects, Grades

# Register your models here.
admin.site.register(Quarters)
admin.site.register(Subjects)
admin.site.register(Grades)
