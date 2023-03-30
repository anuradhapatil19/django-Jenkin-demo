from django.shortcuts import render
from rest_framework import viewsets

from appone.models import Student
from appone.serializers import StudentSerializer


# Create your views here.
class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer