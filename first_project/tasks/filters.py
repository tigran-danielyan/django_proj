from django.db.models import Q
from django_filters import rest_framework as filters
from tasks.models import Task


class TaskFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    description = filters.CharFilter(field_name="description", lookup_expr="icontains")
    q_str = filters.CharFilter(method="name_description_filter")
    cat_name = filters.CharFilter(method="category_name")

    class Meta:
        model = Task
        fields = ["name", "status", "created_at", "description"]

    def name_description_filter(self, qs, name, value):
        new_qs = qs.filter(Q(name__icontains=value) | Q(description__icontains=value))
        return new_qs

    def category_name(self, qs, name, value):
        return qs.filter(category__name__icontains=value)
