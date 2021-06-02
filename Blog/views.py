from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from posts.models import Category,Post
from .forms import CreateCategoryForm,CreatePostForm


def get_categories(request):
    categories= Category.objects.all()
    main_content_var = "Categories"
    context = {'categories':categories,'mainContentVar': main_content_var}
    return render(request, 'admin/categories/categories.html', context)


def add_category(request):
    if request.method == "POST":
        category_form = CreateCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect("/dashboard/categories")
    else:
        category_form = CreateCategoryForm()
        context = {'category_form': category_form}
        return render(request, 'admin/categories/createCategory.html', context) 
        

def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return HttpResponseRedirect("/dashboard/categories")  


def edit_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        category_form = CreateCategoryForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect("/dashboard/categories")
    else:
        category_form = CreateCategoryForm(instance=category)
        context = {'category_form': category_form}
        return render(request, 'admin/categories/createCategory.html', context)               


def get_posts(request):
    posts = Post.objects.all()
    main_content_var = "Posts"
    context = {'posts': posts, 'mainContentVar': main_content_var}
    return render(request, 'admin/posts/postsList.html', context)


def add_post(request):
   
    if request.method == "POST":
        post_form = CreatePostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect("/dashboard/posts")
    else:
        post_form = CreatePostForm()
        context = {'post_form': post_form}
        return render(request, 'admin/posts/createPost.html', context)     


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/dashboard/posts")


