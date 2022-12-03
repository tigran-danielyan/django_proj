from django.shortcuts import HttpResponse
from tasks.models import Task


def home_view(request):
    print("request",  request)
    return HttpResponse("Hello from django")


def create_task(request):
    # new_task = Task(
    #     name="task_3",
    #     description="desc_2"
    # )
    # new_task.save()

    new_task = Task.objects.create(name="task_4")
    return HttpResponse(f"task {new_task}")


def get_all_tasks(request):
    print(request.GET)
    status = request.GET.get("status")
    if status is not None:
        task_list = Task.objects.filter(status=status, name="task_4")
    else:
        task_list = Task.objects.all()
    tasks = [task.name for task in task_list]
    return HttpResponse(f"tasks, {tasks}")


def update_task(request, task_id):

    Task.objects.filter(id=task_id).update(name="updated_1")
    task_ = Task.objects.filter(id=task_id).first()
    # or
    # task_ = Task.objects.get(id=task_id)
    # task_.name = "updated"
    # task_.save()

    return HttpResponse(f"tasks, {task_}")
