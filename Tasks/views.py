from django.shortcuts import render,redirect, get_object_or_404
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def task_form(request):
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            form = TaskForm()
    else:
        form = TaskForm()
    return render(request,"task.html",{"form":form})

@login_required
def task_list(request):

    tasks = Task.objects.all()
    return render(request,"task_list.html",{"tasks":tasks})

@login_required
def task_update(request,id):
    task = get_object_or_404(Task,id=id)

    if request.method == "POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request,"update_task.html",{"form":form})

@login_required
def delete_task(request, id):
    task = get_object_or_404(Task,id=id)
    task.delete()
    return redirect("task_list")
    
