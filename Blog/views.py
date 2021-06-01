from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from posts.models import Post, Category, ForrbiddenWord
# import forms


# Create your views here.
# users
def get_dashboard(request):
    return render(request, 'layouts/dashboard/base.html')


def get_users(request):
    users = User.objects.all()
    title = "Users"
    context = {'title': title, 'users': users}
    return render(request, 'users/_index.html', context)


=======
from django.http import HttpResponse,HttpResponseRedirect
from posts.models import Category,Post
from .forms import createCategoryForm


def get_categories(request):
    categories= Category.objects.all()
    main_content_var = "Categories"
    context = {'categories':categories,'mainContentVar': main_content_var}
    return render(request, 'admin/content/categories.html', context)


def add_category(request):
    if request.method == "POST":
        category_form = createCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect("/blogs/categories")
    else:
        category_form = createCategoryForm()
        context = {'category_form': category_form}
        return render(request, 'admin/content/createCategory.html', context) 
        

def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return HttpResponseRedirect("/blogs/categories")  


def edit_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        category_form = createCategoryForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect("/blogs/categories")
    else:
        category_form = createCategoryForm(instance=category)
        context = {'category_form': category_form}
        return render(request, 'admin/content/createCategory.html', context)               


def get_posts(request):
    posts = Post.objects.all()
    main_content_var = "Posts"
    context = {'posts': posts, 'mainContentVar': main_content_var}
    return render(request, 'admin/content/postsList.html', context) 


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/blogs/posts")
>>>>>>> 923bb2f3dc86a6a3f31cffa141da633d9760ac1c
