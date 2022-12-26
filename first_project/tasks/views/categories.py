from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# new for ClassBasedViews
from rest_framework.views import APIView
from rest_framework import generics

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


@api_view(["DELETE"])
def delete_category(request, category_id):

    try:
        Category.objects.get(id=category_id).delete()
    except Category.DoesNotExist:
        return Response({"message": "Category does not exist"}, status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_204_NO_CONTENT)


#  tasks/ POST create
#  tasks/ GET list
#  tasks/{task_id} GET retrieve
#  tasks/{task_id} PATCH update
#  tasks/{task_id} DELETE delete


class CategoryView(APIView):
    """
    endpoint will be categories/
    """

    def get(self, request):
        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryDetailView(APIView):

    def get_object(self, category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({"message": "Category does not exist"}, status=status.HTTP_404_NOT_FOUND)

        return category

    def get(self, request, category_id):
        category = self.get_object(category_id)
        serializer = CategorySerializer(category)

        return Response(serializer.data)

    def patch(self, request, category_id):
        category = self.get_object(category_id)
        serializer = CategorySerializer(category, data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, category_id):
        self.get_object(category_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryGenericView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = "category_id"  # or pass pk from url
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



"""3, 4
 A recipe search app: This app would allow users to search for recipes based on ingredients, cuisine type,
  or other criteria. It could include features like the ability to save favorite recipes,
    and leave reviews for other users. top 10 recipes
    

1, 2 could include features like the ability to upload and share photos, send private messages, and create groups or communities.

2. A social media platform that allows users to create profiles, share posts, and follow each other. This project can include features such as user authentication,
 a feed of posts from the people the user follows,
  and the ability to like and comment on posts.
  Can block other user


1. Vahe, Norayr, Ararat
2. Mihran, Arthur, Natali
3. Manushak, Ariga
4. Garik, Davit
"""