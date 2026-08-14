from django.urls import path
from .views import task_form,task_list,task_update
urlpatterns = [
    path("create/",task_form),
    path("list/",task_list, name="task_list"),
    path("update/<int:id>/", task_update, name="update_task"),
]