from django.urls import path
from tasks import views

urlpatterns = [
    path("home/", views.home_view),
    path("create/", views.create_task),
    path("tasks/", views.get_all_tasks),
    path("tasks/<int:task_id>/update/", views.update_task),
]
