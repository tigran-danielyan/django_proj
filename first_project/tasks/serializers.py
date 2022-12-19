from rest_framework import serializers

from tasks.models import Task, Category
from users.serializers import UserSerializer


class TaskModelSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField()

    class Meta:
        model = Task
        # fields = "__all__"
        fields = ("id", "name", "description", "status", "created_at", "category", "user")
        # exclude = ("id",)

    # def to_internal_value(self, data):
    #     print("from internal value", data)
    #     return super().to_internal_value(data)
    #
    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = data.pop("user")
        data["user"] = UserSerializer(user).data

        return data


class TaskModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = "__all__"
        fields = ("id", "name", "description", "status", "created_at", "category")
        # exclude = ("id",)



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TaskUpdateModelSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(required=False, max_length=50)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Task
        fields = ("id", "name", "description", "status", "category")

