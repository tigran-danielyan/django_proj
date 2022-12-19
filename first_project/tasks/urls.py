from django.urls import path
from tasks.views import tasks, categories

urlpatterns = [
    path("create/", tasks.create_task),
    # path("tasks/", tasks.get_all_tasks),

]


api_urls = [
    path("", tasks.TaskApiView.as_view()),
    path("find/", tasks.TaskFindView.as_view()),
    path("<int:task_id>/", tasks.TaskDetailView.as_view()),
    # path("categories/create/", categories.create_category),
    # path("categories/", categories.get_categories),
    path("categories/", categories.CategoryGenericView.as_view()),
    # path("categories/", categories.CategoryGenericView.as_view()),
    path("categories/<int:category_id>/", categories.CategoryDetailGenericView.as_view()),
]

urlpatterns.extend(api_urls)
