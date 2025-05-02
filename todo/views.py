from django.http import HttpResponse
from django.shortcuts import redirect, render
from todo.models import Task

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task , is_completed=True)
    return redirect('home')
