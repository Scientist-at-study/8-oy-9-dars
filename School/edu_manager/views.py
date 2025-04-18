from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Teacher, Class, Student
from .serializers import (ClassSerializer, StudentSerializer,
                          StudentStringSerializer, StudentPrimaryKeySerializer,
                          StudentSlugSerializer, StudentHyperlinkedRelatedSerializer,
                          StudentHyperlinkedIdentitySerializer, ClassWithStudentsSerializer,
                          TeacherWithPrimaryKeySerializer, TeacherWithNestedClassesSerializer)

# Create your views here.


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherWithNestedClassesSerializer


class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassWithStudentsSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentHyperlinkedIdentitySerializer