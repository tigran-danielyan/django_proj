from rest_framework import serializers

from tasks.models import Task, Category


class TaskSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    description = serializers.CharField(required=False)
    status = serializers.IntegerField()
    created_at = serializers.DateTimeField(required=False)


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = "__all__"
        fields = ("id", "name", "description", "status", "created_at")
        # exclude = ("id",)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
