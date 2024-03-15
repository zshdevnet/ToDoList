from django.shortcuts import render
from django.http import HttpResponse

def addTask(request):
    return HttpResponse('The form is submited')