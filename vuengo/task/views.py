from django.shortcuts import render
import rest_framework
from rest_framework import authentication
from rest_framework.decorators import permission_classes
from rest_framework.serializers import Serializer

# Create your views here.
from .models import Task

from .serializers import TaskSerializer

from  rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    