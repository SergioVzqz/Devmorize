from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse

# Create your views here.
def taskList(request):
    return HttpResponse('To do list')