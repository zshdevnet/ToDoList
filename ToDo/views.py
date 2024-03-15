from django.shortcuts import render
from django.http import HttpResponse
from todos.models import Task

def home(request):
    tasks_false = Task.objects.filter(is_completed=False)
    tasks_true = Task.objects.filter(is_completed=True)
    context = {
        'tasks_false' : tasks_false,
        'tasks_true' : tasks_true,
    }
    return render(request, 'home.html', context)