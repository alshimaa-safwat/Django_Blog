from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post , Comments, Reaction ,BadWord
import json
import re
from .forms import postForm
from django.core.paginator import Paginator
from django.core.mail import send_mail

# Create your views here.

# add comment function
def addComment(request,postid): #the worst function i had done shitty code i know 
	if request.method=="POST":
		post= Post.objects.get(id=postid)
		uname = request.user # we have to replace it with auth user 
		con = request.POST.get('message')
		mptrn= r"^[\S][\S ]+$"
		result = re.match(mptrn, con)
		if (result):
			#]
			words =BadWord.objects.all()
			for word in words:
				rep=""
				size=len(word.word)
				for i in range(size):
					rep+="*"
				con = con.replace(word.word,rep)
			comm = Comments(post_name=post,user_name=uname,content=con)
			comm.save()
		
		return HttpResponseRedirect('/posts/'+postid )


# delete comment function
def deletecomment(request,comid):
	comment = Comments.objects.get(id=comid)
	postid = comment.post_name_id
	if(request.user==comment.user_name or request.user.is_staff):
		comment.delete()
	return HttpResponseRedirect('/posts/'+str(postid))
