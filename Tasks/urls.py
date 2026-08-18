from django.urls import path
from .views import *
urlpatterns = [
    path("create/",task_form, name="task_create"),
    path("list/",task_list, name="task_list"),
    path("update/<int:id>/", task_update, name="update_task"),
    path("delete/<int:id>/",delete_task, name="task_delete")
]