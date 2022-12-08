from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from tasks.models import Category
from tasks.serializers import (
    CategorySerializer
    )


@api_view(["POST"])
def create_category(request):
    serializer = CategorySerializer(data=request.data)

    serializer.is_valid(raise_exception=True)

    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_categories(request):

    categories = Category.objects.all()

    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PATCH"])
def update_category(request, category_id):

    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({"message": "Category does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category, data=request.data)

    serializer.is_valid(raise_exception=True)

    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PATCH"])
def update_category(request, category_id):

    try:
        Category.objects.get(id=category_id).delete()
    except Category.DoesNotExist:
        return Response({"message": "Category does not exist"}, status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_204_NO_CONTENT)
