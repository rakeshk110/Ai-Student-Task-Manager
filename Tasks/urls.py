from django.urls import path
from .views import *
urlpatterns = [
    path("create/",task_form, name="task_create"),
    path("list/",task_list, name="task_list"),
    path("update/<int:id>/", task_update, name="update_task"),
    path("suggest/", ai_suggest, name="ai_suggest"),
    path("complete/<int:id>/", task_complete, name="task_complete"),
    path("delete/<int:id>/",delete_task, name="task_delete")
]