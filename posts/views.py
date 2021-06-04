from django.core import paginator
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ForbiddenWord, Post, Category, Comment, Reply, Reaction, Subscribe, Tag
import json
import re
from .forms import PostForm
from django.core.paginator import Paginator
from django.core.mail import send_mail


def get_subscribe_data(request):
    userId = request.user.id
    catNum = request.GET['catNum']
    refresh = request.GET['refresh']
    cat = []
    sub = []
    if refresh == '1':
        subscribes = Subscribe
        for x in subscribes.objects.filter(user_id=userId):
            if x.user.id == userId:
                cat.append(x.Category.id)
            else:
                pass
    else:
        subscribes, created = Subscribe.objects.get_or_create(
            user_id=userId, Category_id=catNum)
        if created == True:
            cat.append(subscribes.Category.id)
            try:
                user = request.user
                cato = Category.objects.get(id=catNum)
                subject = 'category subscription'
                message = 'u have subscibed in :' + cato.name + \
                    ' use this url to visit this category http://127.0.0.1:8000/posts/listcat/' + \
                    str(cato.id)
                recepient = user.email
                send_mail(subject, message, 'osamaeltayar011100',
                          [recepient], fail_silently=False)
            except Exception as e:
                print(e)

        else:
            subscribes.delete()
    return HttpResponse(json.dumps({'categoryNum': cat}))


def add_Comment(request, postid):  # the worst function i had done shitty code i know
    if request.method == "POST":
        post = Post.objects.get(id=postid)
        uname = request.user  # we have to replace it with auth user
        con = request.POST.get('message')
        mptrn = r"^[\S][\S ]+$"
        result = re.match(mptrn, con)
        if (result):
            words = ForbiddenWord.objects.all()
            for word in words:
                rep = ""
                size = len(word.word)
                for i in range(size):
                    rep += "*"
                con = con.replace(word.word, rep)
            comm = Comment(post=post, user=uname, content=con)
            comm.save()

        return HttpResponseRedirect('/posts/'+postid)


def delete_comment(request, comid):
    comment = Comment.objects.get(id=comid)
    postid = comment.post_id
    if(request.user == comment.user or request.user.is_staff):
        comment.delete()
    return HttpResponseRedirect('/posts/'+str(postid))


def add_reply(request, comid):
    if request.method == "POST":
        comment = Comment.objects.get(id=comid)
        uname = request.user
        con = request.POST.get('message')
        mptrn = r"^[\S][\S ]+$"
        result = re.match(mptrn, con)
        if(result):
            words = ForbiddenWord.objects.all()
            for word in words:
                rep = ""
                size = len(word.word)
                for i in range(size):
                    rep += "*"
                con = con.replace(word.word, rep)
            rep = Reply(user=uname, comment=comment, content=con)
            rep.save()
        return HttpResponseRedirect('/posts/'+str(comment.post_id))


def delete_reply(request, repid):
    reply = Reply.objects.get(id=repid)
    comment = Comment.objects.get(id=reply.comment_id)
    if(request.user == reply.user or request.user.is_staff):
        reply.delete()
    return HttpResponseRedirect('/posts/'+str(comment.post_id))


def add_tag(request):
    if request.method == "POST":
        con = request.POST.get('othertag')
        tagPtrn = r"^#[\S]+$"
        newTag = con.split(" ")
        flag = 1
        for ourTag in newTag:
            if(re.match(tagPtrn, ourTag)):
                allTags = Tag.objects.all()
                for eachTag in allTags:
                    if(eachTag.tag == ourTag):
                        flag = 0
                    else:
                        continue
                if flag == 1:
                    ta = Tag(tag=ourTag)
                    ta.save()
    return HttpResponseRedirect('/posts/newPost')


def list_tags(request, tagid):
    tag = Tag.objects.get(id=tagid)
    posts = Post.objects.filter(tag=tag)
    cats = Category.objects.all()
    context = {'posts': posts, 'cats': cats}
    return render(request, 'posts/index.html', context)


# add comment function

def about(request):
    cats = Category.objects.all()
    return render(request, 'posts/about.html', {'cats': cats})


def list_cat(request, catid):
    posts = Post.objects.filter(category_id=catid)
    cats = Category.objects.all()
    context = {'posts': posts, 'cats': cats}
    return render(request, 'posts/index.html', context)


def add_comment(request, postid):  # the worst function i had done shitty code i know
    if request.method == "POST":
        post = Post.objects.get(id=postid)
        uname = request.user  # we have to replace it with auth user
        con = request.POST.get('message')
        mptrn = r"^[\S][\S ]+$"
        result = re.match(mptrn, con)
        if (result):
            words = ForbiddenWord.objects.all()
            for word in words:
                rep = ""
                size = len(word.word)
                for i in range(size):
                    rep += "*"
                con = con.replace(word.word, rep)
            comm = Comment(post=post, user=uname, content=con)
            comm.save()

        return HttpResponseRedirect('/posts/' + postid)


# delete comment function
def delete_comment(request, comid):
    comment = Comment.objects.get(id=comid)
    postid = comment.post_id
    if (request.user == comment.user or request.user.is_staff):
        comment.delete()
    return HttpResponseRedirect('/posts/' + str(postid))


# get like data function
def get_like_data(request):
    postId = request.GET['postId']
    userId = request.user.id
    print(userId)
    reactState = request.GET['reactStatex']
    refresh = request.GET['refreshx']
    reaction, created = Reaction.objects.get_or_create(
        post_id=postId, user_id=userId)
    if(refresh == '0'):
        reaction.react = reactState
        reaction.save()
    else:
        pass
    likeReact = Reaction.objects.filter(post_id=postId, react="like").count()
    dislikeReact = Reaction.objects.filter(
        post_id=postId, react="dislike").count()

    return HttpResponse(json.dumps({'reactType': reaction.react, 'likeReact': likeReact, 'dislikeReact': dislikeReact}))


# by Shendi


def home_page(request):
    posts = Post.objects.all().order_by('date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)
    for post in posts:
        dislikes = Reaction.objects.filter(
            react="dislike", post=post.id).count()
        if dislikes == 10:
            post.delete()
    categories = Category.objects.all()
    return render(request, 'posts/index.html', {'posts': page, 'categories': categories})


def display_post(request, post_id):
    post = Post.objects.get(id=post_id)
    categories = Category.objects.all()
    comments = Comment.objects.filter(post_id=post_id)

    data = []
    for comment in comments:
        try:
            replies = Reply.objects.filter(comment_id=comment.id)
            data.append({'comment': comment, 'replies': replies})
        except Exception as e:
            data.append({"comment": comment})

    return render(request, 'posts/post.html', {'post': post, 'data': data, 'categories': categories})


def add_post(request):
    if request.method == 'POST':
        post = PostForm(request.POST, request.FILES, Post)
        if post.is_valid():
            new_post = post.save(commit=False)
            new_post.author = request.user
            new_post.thumbnail = request.FILES.get('thumbnail')
            new_post.save()
            return HttpResponseRedirect('/posts/')
    else:
        post = PostForm()

    categories = Category.objects.all()
    return render(request, 'posts/new.html', {'post': post, 'categories': categories, 'status': 'New'})


def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if(request.user == post.author or request.user.is_staff):
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.thumbnail = request.FILES.get('thumbnail')
                new_form.save()
                return HttpResponseRedirect('/posts/')
        else:
            form = PostForm(instance=post)
            categories = Category.objects.all()
            return render(request, 'posts/new.html', {'post': form, 'categories': categories, 'status': "Edit"})
    else:
        return HttpResponseRedirect('/posts/')


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if(request.user == post.author or request.user.is_staff):
        post.delete()
    return HttpResponseRedirect('/posts/')
