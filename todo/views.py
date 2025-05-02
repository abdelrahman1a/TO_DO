from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from todo.models import Task

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task , is_completed=True)
    return redirect('home')

def mark_as_done(request , pk):
    task = get_object_or_404(Task , pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request , pk):
    task = get_object_or_404(Task , pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


def EditTask(request , pk):
    get_task = get_object_or_404(Task , pk=pk)
    if request.method == "POST":
        new_task = request.POST["task"] # getting value in the input
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task' : get_task,
        }
        return render(request , "EditTask.html" , context)
    
def Delete_Task(request , pk):
    task = get_object_or_404(Task , pk=pk)
    task.delete()
    return redirect('home')