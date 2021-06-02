from django.db import models

# Create your models here.


class Reply(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	comment = models.ForeignKey(Comments,on_delete=models.CASCADE)
	content = models.CharField(max_length=200)
	date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s %s' % (self.user, self.comment)

class Subscribe(models.Model):
	user =models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
	Category =models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return '%s %s' % (self.user, self.cat)


class ForrbiddenWord(models.Model):
	word =models.CharField(max_length=10)

	def __str__(self):
		return self.word