from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from posts.models import Post, Category, ForrbiddenWord
from .forms import createCategoryForm, CreateUserForm

def get_dashboard(request):
    return render(request, 'admin/adminlte.html')


def get_users(request):
    users = User.objects.all()
    title = "Users"
    context = {'title': title, 'users': users}
    return render(request, 'admin/users/index.html', context)


def create_user(request):
    if request.method == "POST":
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect("/dashboard/users")
    else:
        user_form = CreateUserForm()
        context = {'user_form': user_form}
        return render(request, 'admin/users/create_user.html', context)


def edit_user(request, id):
    user = User.objects.get(id=id)
    context = {'user': user}
    # if user.is_staff:
    #     # ??????????????????
    #     return render(request, 'ourBlog/posts', context)
    # else:
    return render(request, 'admin/users/edit_user.html', context)


def update_user(request, id):
    if request.POST.get('cancel'):
        return HttpResponseRedirect("/dashboard/users")
    else:
        user = User.objects.get(id=id)
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return HttpResponseRedirect("/dashboard/users")


def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return HttpResponseRedirect("/dashboard/users")

    except User.DoesNotExist:
        return HttpResponseRedirect("/dashboard/users")


def get_categories(request):
    categories = Category.objects.all()
    main_content_var = "Categories"
    context = {'categories': categories, 'mainContentVar': main_content_var}
    return render(request, 'admin/includes/categories.html', context)


def add_category(request):
    if request.method == "POST":
        category_form = createCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect("/blogs/categories")
    else:
        category_form = createCategoryForm()
        context = {'category_form': category_form}
        return render(request, 'admin/includes/createCategory.html', context)


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
        return render(request, 'admin/includes/createCategory.html', context)


def get_posts(request):
    posts = Post.objects.all()
    main_content_var = "Posts"
    context = {'posts': posts, 'mainContentVar': main_content_var}
    return render(request, 'admin/includes/postsList.html', context)


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/blogs/posts")


def add_post(request):
   
    if request.method == "POST":
        post_form = createCategoryForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect("/dashboard/posts")
    else:
        post_form = createCategoryForm )
        context = {'post_form': post_form}
        return render(request, 'admin/posts/createPost.html', context)    
