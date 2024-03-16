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

def undoneTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def editTask(request, pk):
    getTask = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        getTask.task = new_task
        getTask.save()
        return redirect('home')
    else:
        context = {
            'getTask': getTask,
        }
    return render(request, 'editTask.html', context)


def delTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')