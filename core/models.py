from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
