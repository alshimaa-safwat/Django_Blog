from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from posts.models import Post, Category, ForbiddenWord
from .forms import CreateCategoryForm, CreateUserForm, CreatePostForm, CreateBadWordForm


def words(request):
    word = ForbiddenWord.objects.all()
    mainContentVar = "Forbidden Words"
    context = {'word': word, 'mainContentVar': mainContentVar}
    return render(request, 'admin/words/wordsForbidden.html', context)


def delete_word(request, id):
    word = ForbiddenWord.objects.get(id=id)
    word.delete()
    return HttpResponseRedirect("/dashboard/words")


def add_word(request):
    if request.method == "POST":
        bad_word_form = CreateBadWordForm(request.POST)
        if bad_word_form.is_valid():
            bad_word_form.save()
            return HttpResponseRedirect("/dashboard/words")
    else:
        bad_word_form = CreateBadWordForm()
        context = {'badWord_form': bad_word_form}
        return render(request, 'admin/words/createBadWord.html', context)


def edit_word(request, id):
    word = ForbiddenWord.objects.get(id=id)
    if request.method == "POST":
        bad_word_form = CreateBadWordForm(request.POST, instance=word)
        if bad_word_form.is_valid():
            bad_word_form.save()
            return HttpResponseRedirect("/dashboard/words")
    else:
        bad_word_form = CreateBadWordForm(instance=word)
        context = {'badWord_form': bad_word_form}
        return render(request, 'admin/words/createBadWord.html', context)


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


def lock_user(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect('/dashboard/users')


def unlock_user(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect('/dashboard/users')


def upgrade_user(request, id):
    user = User.objects.get(id=id)
    user.is_staff = True
    user.is_admin = True
    user.is_superuser = True
    user.save()
    return HttpResponseRedirect("/dashboard/users")


def downgrade_user(request, id):
    user = User.objects.get(id=id)
    user.is_staff = False
    user.is_admin = False
    user.is_superuser = False
    user.save()
    return HttpResponseRedirect("/dashboard/users")


def get_categories(request):
    categories = Category.objects.all()
    main_content_var = "Categories"
    context = {'categories': categories, 'mainContentVar': main_content_var}
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


def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect("/dashboard/posts")


def add_post(request):
    if request.method == "POST":
        post = CreatePostForm(request.POST, request.FILES)
        if post.is_valid():
            new_post = post.save(commit=False)
            new_post.author = request.user
            new_post.thumbnail = request.FILES.get('thumbnail')
            new_post.save()
            return HttpResponseRedirect("/dashboard/posts")
    else:
        post_form = CreatePostForm()
        context = {'post_form': post_form}
        return render(request, 'admin/posts/createPost.html', context)


def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        post = CreatePostForm(request.POST, request.FILES, instance=post)
        if post.is_valid():
            new_post = post.save(commit=False)
            new_post.author = request.user
            if(request.FILES.get('thumbnail') != None):
                new_post.thumbnail = request.FILES.get('thumbnail')
            new_post.save()
            return HttpResponseRedirect("/dashboard/posts")
    else:
        post_form = CreatePostForm(instance=post)
        context = {'post_form': post_form}
        return render(request, 'admin/posts/createPost.html', context)
