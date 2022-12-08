from django.shortcuts import HttpResponse
# new
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from tasks.models import Task, Category
from tasks.serializers import (
    TaskSerializer,
    TaskModelSerializer,
    CategorySerializer
    )



#
# def create_task(request):
#     # new_task = Task(
#     #     name="task_3",
#     #     description="desc_2"
#     # )
#     # new_task.save()
#
#     new_task = Task.objects.create(name="task_4")
#     return HttpResponse(f"task {new_task}")
#
#
# def get_all_tasks(request):
#     print(request.GET)
#     status = request.GET.get("status")
#     if status is not None:
#         task_list = Task.objects.filter(status=status, name="task_4")
#     else:
#         task_list = Task.objects.all()
#
#
#     tasks = [task.name for task in task_list]
#
#     return HttpResponse(f"tasks, {tasks}")
#
#
# def update_task(request, task_id):
#
#     Task.objects.filter(id=task_id).update(name="updated_1")
#     task_ = Task.objects.filter(id=task_id).first()
#     # or
#     # task_ = Task.objects.get(id=task_id)
#     # task_.name = "updated"
#     # task_.save()
#
#     return HttpResponse(f"tasks, {task_}")
#
#
# @api_view(["GET"])
# def get_task(request, task_id):
#
#     task = Task.objects.get(id=task_id)
#
#     serialized_task = TaskSerializer(task)
#
#     return Response(serialized_task.data)
#
#
# # @api_view(["POST"])
# # def create_task_view(request):
# #     print("*"*10, request.data)
# #     serializer = TaskSerializer(data=request.data)
# #
# #     serializer.is_valid(raise_exception=True)
# #
# #     print(serializer.data, serializer.errors)
# #
# #     task = Task.objects.create(**serializer.data)
# #     # task = Task.objects.create(
# #     #     name=serializer.data["name"],
# #     #     description=serializer.data["description"],
# #     #     status=serializer.data["status"]
# #     # )
# #
# #     serializer = TaskSerializer(task)
# #
# #     return Response(serializer.data)
#
# @api_view(["POST"])
# def create_task_view(request):
#     serializer = TaskModelSerializer(data=request.data)
#
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(["GET"])
# def get_tasks(request):
#
#     category_id = request.GET.get("category_id")
#
#     tasks = Task.objects.all()
#
#     if category_id:
#         try:
#             category = Category.objects.get(id=category_id)
#         except Category.DoesNotExists:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
#         tasks = category.task_set.all()  # the same as
#         # tasks = Task.objects.filter(category=category)
#
#     serializer = TaskModelSerializer(tasks, many=True)
#
#     return Response(serializer.data)


# @api_view(["POST"])
# def create_category(request):
#     serializer = CategorySerializer(data=request.data)
#
#     serializer.is_valid(raise_exception=True)
#
#     serializer.save()
#
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(["GET"])
# def get_categories(request):
#
#     categories = Category.objects.all()
#
#     serializer = CategorySerializer(categories, many=True)
#
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(["PATCH"])
# def update_category(request, category_id):
#
#     try:
#         category = Category.objects.get(id=category_id)
#     except Category.DoesNotExist:
#         return Response({"message": "Category does not exist"}, status=status.HTTP_404_NOT_FOUND)
#
#     serializer = CategorySerializer(category, data=request.data)
#
#     serializer.is_valid(raise_exception=True)
#
#     serializer.save()
#
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(["PATCH"])
# def update_category(request, category_id):
#
#     try:
#         Category.objects.get(id=category_id).delete()
#     except Category.DoesNotExist:
#         return Response({"message": "Category does not exist"}, status=status.HTTP_404_NOT_FOUND)
#
#     return Response(status=status.HTTP_204_NO_CONTENT)










