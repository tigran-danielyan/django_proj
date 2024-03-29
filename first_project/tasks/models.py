from django.contrib.auth.models import User
from django.db import models

STATUS_CHOICES = (
    (0, "new"),
    (1, "doing"),
    (2, "done")
)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="task_set")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}-{self.status}"

