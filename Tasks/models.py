from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):


    CATEGORY_CHOICES =[
        ('assignment','Assignment'),
        ('project','Project'),
        ('exam','Exam'),
        ('internship','Internship'),
        ('personal','Personal'),
    ]
    PRIORITY_CHOICES =[
        ('low','Low'),
        ('medium','Medium'),
        ('high','High')
    ]
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('in_progress','In Progress'),
        ('completed','Completed')
    ]

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    priority = models.CharField(
        max_length=20,
        default='medium',
        choices=PRIORITY_CHOICES

    )
    status = models.CharField(
        max_length=20,
        default='pending',
        choices=STATUS_CHOICES
    )

    due_date = models.DateField(
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(
        auto_now_add=True
    )
    update_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

