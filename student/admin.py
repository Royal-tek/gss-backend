from django.contrib import admin
from .models import Pupil, Parent, Teacher, Classes

admin.site.register(Pupil)
admin.site.register(Parent)
admin.site.register(Teacher)
admin.site.register(Classes)
