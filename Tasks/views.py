from django.shortcuts import render,redirect, get_object_or_404
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def task_form(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.student = request.user
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "task.html", {"form": form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(student=request.user)
    return render(
        request,
        "task_list.html",
        {
            "tasks": tasks,
            "pending_count": tasks.filter(status="pending").count(),
            "in_progress_count": tasks.filter(status="in_progress").count(),
            "completed_count": tasks.filter(status="completed").count(),
        },
    )

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
def task_complete(request, id):
    task = get_object_or_404(Task, id=id, student=request.user)
    task.status = "completed"
    task.save()
    return redirect("task_list")

@login_required
def ai_suggest(request):
    from datetime import date

    tasks = Task.objects.filter(student=request.user).exclude(status="completed")

    def score(task):
        s = 0
        # Priority
        if task.priority == "high":
            s += 3
        elif task.priority == "medium":
            s += 2
        else:
            s += 1
        # Status
        if task.status == "in_progress":
            s += 1
        elif task.status == "pending":
            s += 2
        # Due date urgency
        if task.due_date:
            diff = (task.due_date - date.today()).days
            if diff < 0:
                s += 5
            elif diff == 0:
                s += 4
            elif diff <= 2:
                s += 3
            elif diff <= 7:
                s += 2
            else:
                s += 1
        # Category weight
        if task.category in ("exam", "assignment"):
            s += 1
        return s

    def build_reason(task):
        parts = []
        parts.append(f"{task.get_priority_display()} priority")
        if task.due_date:
            diff = (task.due_date - date.today()).days
            if diff < 0:
                parts.append("already overdue")
            elif diff == 0:
                parts.append("due today")
            elif diff <= 2:
                parts.append("due very soon")
            elif diff <= 7:
                parts.append(f"due in {diff} days")
        else:
            parts.append("no deadline pressure")
        if task.status == "in_progress":
            parts.append("already started — easier to finish")
        elif task.status == "pending":
            parts.append("ready to begin")
        if task.category in ("exam", "assignment"):
            parts.append(f"category: {task.get_category_display()}")
        return "Recommended because it is " + ", ".join(parts) + "."

    ranked = sorted(tasks, key=score, reverse=True)

    primary = None
    secondary = None

    if ranked:
        primary = {"title": ranked[0].title, "reason": build_reason(ranked[0])}
    if len(ranked) > 1:
        secondary = {"title": ranked[1].title, "reason": build_reason(ranked[1])}

    if not primary:
        primary = {"title": "All tasks completed!", "reason": "Great work. Nothing urgent left."}
    if not secondary:
        secondary = {"title": "No alternate task", "reason": "Focus on the primary suggestion above."}

    all_tasks = Task.objects.filter(student=request.user)
    return render(
        request,
        "task_list.html",
        {
            "tasks": all_tasks,
            "pending_count": all_tasks.filter(status="pending").count(),
            "in_progress_count": all_tasks.filter(status="in_progress").count(),
            "completed_count": all_tasks.filter(status="completed").count(),
            "ai_primary": primary,
            "ai_secondary": secondary,
            "show_ai": True,
        },
    )

@login_required
def delete_task(request, id):
    task = get_object_or_404(Task,id=id)
    task.delete()
    return redirect("task_list")
    
