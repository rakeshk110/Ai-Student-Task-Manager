from django.shortcuts import render
from .forms import TaskForm

def form(request):
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            form = TaskForm()
    else:
        form = TaskForm()
    return render(request,"task.html",{"form":form})

