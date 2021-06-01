# Create your models here.
<<<<<<< HEAD
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
=======
from django.contrib.auth.models import User
from django.db import models


class ExtendedUser():
    pass
>>>>>>> 923bb2f3dc86a6a3f31cffa141da633d9760ac1c
