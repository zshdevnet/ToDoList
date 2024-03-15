from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

def addTask(request):
    task = request.POST.get('task')
    Task.objects.create(task=task)
    return redirect('home')

def doneTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def delTask(request):
    pass
    return redirect('home')