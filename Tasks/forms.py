from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'category',
            'priority',
            'status',
            'due_date',
        ]
        widgets = {
            "title":forms.TextInput(attrs={
                "class":"task-input",
                "placeholder":"Enter Task"
            }),
            "student":forms.Select(attrs={
                "class":"task-input",
            }),
            "description":forms.TextInput(attrs={
                "class":"task-input",
                "placeholder":"Enter description"
            }),
            "category":forms.Select(attrs={
                "class":"task-input",
            }),
            "status":forms.Select(attrs={
                "class":"task-input",
            }),
            "priority":forms.Select(attrs={
                "class":"task-input",
            }),
            "due_date":forms.TextInput(attrs={
                "class":"task-input",
                "placeholder":"select due date"
            }),
        }
