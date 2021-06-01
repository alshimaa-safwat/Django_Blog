from django.db import models
from django.contrib.auth.models import User


class ForrbiddenWord(models.Model):
	word =models.CharField(max_length=10)

	def __str__(self):
		return self.word

 
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    thumbnail = models.ImageField(default='default.png', blank=True)
    tag = models.ManyToManyField(Tag, db_table="PostTags")

    def __str__(self):
        return self.title

    def excerpt(self):
        return self.body[:150] + '...'