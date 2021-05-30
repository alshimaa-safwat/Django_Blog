from django.db import models
from django.contrib.auth.models import User


# Create your models here.
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


# Comment model
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	content = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s %s' % (self.user, self.post)


# Reaction model
class Reaction(models.Model):
	user =models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	post =models.ForeignKey(Post, on_delete=models.CASCADE)
	react =models.CharField(max_length=7, choices = emotion , default='none')

	def __str__(self):
		return '%s %s %s' % (self.post , self.user ,self.react)
