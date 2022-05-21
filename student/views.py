from django.shortcuts import render

from rest_framework import generics
from .models import Pupil, Parent, Teacher
from .serializers import PupilSerializer, ParentSerializer, TeacherSerializer


class StudentView(generics.ListCreateAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer

class ParentView(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class TeacherView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    