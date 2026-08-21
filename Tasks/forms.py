from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "category",
            "priority",
            "status",
            "due_date",
        ]
        labels = {
            "title": "Task Title",
            "description": "Description",
            "category": "Category",
            "priority": "Priority",
            "status": "Status",
            "due_date": "Due Date",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "task-input",
                    "placeholder": "e.g. Complete math assignment",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "task-input task-input--textarea",
                    "placeholder": "Add task details...",
                    "rows": 4,
                }
            ),
            "category": forms.Select(attrs={"class": "task-input"}),
            "status": forms.Select(attrs={"class": "task-input"}),
            "priority": forms.Select(attrs={"class": "task-input"}),
            "due_date": forms.DateInput(
                attrs={
                    "class": "task-input",
                    "type": "date",
                }
            ),
        }
