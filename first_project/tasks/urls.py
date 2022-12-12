from django.urls import path
from tasks.views import tasks, categories

urlpatterns = [
    path("create/", tasks.create_task),
    # path("tasks/", tasks.get_all_tasks),

]


api_urls = [
    path("tasks/<int:task_id>/", tasks.get_task),
    path("tasks/<int:task_id>/update/", tasks.update_task),
    path("tasks/add/", tasks.create_task_view),
    path("tasks/list/", tasks.get_tasks),
    # path("categories/create/", categories.create_category),
    # path("categories/", categories.get_categories),
    path("categories/", categories.CategoryGenericView.as_view()),
    # path("categories/", categories.CategoryGenericView.as_view()),
    path("categories/<int:category_id>/", categories.CategoryDetailGenericView.as_view()),
]

urlpatterns.extend(api_urls)
