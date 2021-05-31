from django.db import models
from django.contrib.auth.models import User


# Category model
class Category(models.Model):
    category_name = models.CharField(max_length=100)






