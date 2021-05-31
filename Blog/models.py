from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Comment(models.Model):
#     body = models.CharField(max_length=100)
#     date = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
#
# # Post model
#
#
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     body = models.TextField()
#     image = models.CharField(max_length=100)
#     # category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now=True)
#
#
# # Category model
# class Category(models.Model):
#     category_name = models.CharField(max_length=100)
