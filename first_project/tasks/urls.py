from django.urls import path
from tasks import views

urlpatterns = [
    path("home/", views.home_view),
    path("create/", views.create_task),
    path("tasks/", views.get_all_tasks),
    path("tasks/<int:task_id>/update/", views.update_task),

]


api_urls = [
    path("tasks/<int:task_id>/", views.get_task),
    path("tasks/add/", views.create_task_view),
    path("tasks/list/", views.get_tasks),
    path("categories/create/", views.create_category),
    path("categories/", views.get_categories),
    path("categories/<int:category_id>/update/", views.update_category),
]

urlpatterns.extend(api_urls)