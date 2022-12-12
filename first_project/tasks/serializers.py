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
        fields = ("id", "name", "description", "status", "created_at", "category")
        # exclude = ("id",)

    # def to_internal_value(self, data):
    #     print("from internal value", data)
    #     return super().to_internal_value(data)
    #
    # def to_representation(self, instance):
    #
    #     data = super().to_representation(instance)
    #     print("from to_representation value ---", data)
    #     data["category"] = CategorySerializer(instance.category).data
    #     return data


class TaskModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = "__all__"
        fields = ("id", "name", "description", "status", "created_at", "category")
        # exclude = ("id",)

    def to_internal_value(self, data):
        print("from internal value", data)
        return super().to_internal_value(data)

    def to_representation(self, instance):
        print("from to_representation value ---")

        return super().to_representation(instance)


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

