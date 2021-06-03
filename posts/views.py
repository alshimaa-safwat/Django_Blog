from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post , Category ,Comment,Reply, Reaction, ForrbiddenWord
import json
import re
from .forms import postForm
from django.core.paginator import Paginator
from django.core.mail import send_mail

# Create your views here.

# add comment function

def about(request):
	cats = Category.objects.all()
	return render(request,'posts/about.html',{'cats':cats})

def list_cat(request,catid):
	posts = Post.objects.filter(category_id=catid)
	cats = Category.objects.all()
	context={'posts':posts,'cats':cats}
	return render(request,'posts/index.html', context)


def add_comment(request, postid):  # the worst function i had done shitty code i know
    if request.method == "POST":
        post = Post.objects.get(id=postid)
        uname = request.user  # we have to replace it with auth user
        con = request.POST.get('message')
        mptrn = r"^[\S][\S ]+$"
        result = re.match(mptrn, con)
        if (result):
            words = ForrbiddenWord.objects.all()
            for word in words:
                rep = ""
                size = len(word.word)
                for i in range(size):
                    rep += "*"
                con = con.replace(word.word, rep)
            comm = Comment(post=post, user=uname, content=con)
            comm.save()

        return HttpResponseRedirect('/posts/'+postid)


# delete comment function
def delete_comment(request, comid):
    comment = Comment.objects.get(id=comid)
    postid = comment.post_id
    if(request.user == comment.user or request.user.is_staff):
        comment.delete()
    return HttpResponseRedirect('/posts/'+str(postid))


# get like data function
def get_like_data(request):
	postId = request.GET['postId']
	userId = request.user.id
	print(userId)
	reactState = request.GET['reactStatex']
	refresh = request.GET['refreshx']
	reaction, created = Reaction.objects.get_or_create(post_id=postId, user_id=userId)
	if(refresh=='0'):
		reaction.react=reactState
		reaction.save()
	else:
		pass
	likeReact = Reaction.objects.filter(post_id=postId, react="like").count()
	dislikeReact = Reaction.objects.filter(post_id=postId, react="dislike").count()

	return HttpResponse(json.dumps({'reactType':reaction.react, 'likeReact':likeReact, 'dislikeReact':dislikeReact}))
