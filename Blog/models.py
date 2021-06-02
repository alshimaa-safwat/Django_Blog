# Create your models here.
from django.contrib.auth.models import User
from django.db import models


<<<<<<< HEAD
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.CharField(max_length=100)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)


# Category model
class Category(models.Model):
    category_name = models.CharField(max_length=100)
=======
class ExtendedUser:
    pass
>>>>>>> 20598bb9e74253e2d98bc9e669ff15713a96def0
