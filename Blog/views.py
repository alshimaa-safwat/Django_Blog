from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from posts.models import Post, Category, ForbiddenWord, Tag
from .forms import CreateCategoryForm, CreateUserForm, CreatePostForm, CreateBadWordForm, CreateTagForm
from django.contrib.auth.decorators import login_required

def check_auth_user_staff(request):
    return request.user.is_staff


@login_required(login_url="/login")
def words(request):
    if check_auth_user_staff(request):
        word = ForbiddenWord.objects.all()
        mainContentVar = "Forbidden Words"
        context = {'word': word, 'mainContentVar': mainContentVar}
        return render(request, 'admin/words/wordsForbidden.html', context)
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def delete_word(request, id):
    if check_auth_user_staff(request):
        word = ForbiddenWord.objects.get(id=id)
        word.delete()
        return HttpResponseRedirect("/dashboard/words")
    else:
        return HttpResponseRedirect('/')


def add_tag(request):
    if request.method == "POST":
        tag_form = CreateTagForm(request.POST)
        if tag_form.is_valid():
            tag_form.save()
            return HttpResponseRedirect("/dashboard/tags")
    else:
        tag_form = CreateTagForm()
        context = {'tag_form': tag_form}
        return render(request, 'admin/tags/createTag.html', context)


def delete_tag(request, id):
    tag = Tag.objects.get(id=id)
    tag.delete()
    return HttpResponseRedirect("/dashboard/tags")


def edit_tag(request, id):
    tag_form = Tag.objects.get(id=id)
    if request.method == "POST":
        tag_form = CreateTagForm(request.POST, instance=tag_form)
        if tag_form.is_valid():
            tag_form.save()
            return HttpResponseRedirect("/dashboard/tags")
    else:
        tag_form = CreateTagForm(instance=tag_form)
        context = {'tag_form': tag_form}
        return render(request, 'admin/tags/createTag.html', context)


def tags(request):
    tags = Tag.objects.all()
    mainContentVar = "tags"
    context = {'tags': tags, 'mainContentVar': mainContentVar}
    return render(request, 'admin/tags/tags.html', context)


@login_required(login_url="/login")
def add_word(request):
    if check_auth_user_staff(request):
        if request.method == "POST":
            bad_word_form = CreateBadWordForm(request.POST)
            if bad_word_form.is_valid():
                bad_word_form.save()
                return HttpResponseRedirect("/dashboard/words")
        else:
            bad_word_form = CreateBadWordForm()
            context = {'badWord_form': bad_word_form}
            return render(request, 'admin/words/createBadWord.html', context)
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def edit_word(request, id):
    if check_auth_user_staff(request):
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
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def get_dashboard(request):
    if check_auth_user_staff(request):
        return render(request, 'admin/adminlte.html')
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def get_users(request):
    if check_auth_user_staff(request):
        users = User.objects.exclude(
            email=request.user.email).exclude(is_superuser=1)
        main_content_var = "Users"
        context = {'users': users, 'mainContentVar': main_content_var}
        return render(request, 'admin/users/index.html', context)
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def create_user(request):
    if check_auth_user_staff(request):
        if request.method == "POST":
            user_form = CreateUserForm(request.POST)
            if user_form.is_valid():
                user_form.save()
                return HttpResponseRedirect("/dashboard/users")
        else:
            user_form = CreateUserForm()
            context = {'user_form': user_form}
            return render(request, 'admin/users/create_user.html', context)
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def edit_user(request, id):
    if check_auth_user_staff(request):
        try:
            user = User.objects.get(id=id)
            context = {'user': user}
            return render(request, 'admin/users/edit_user.html', context)
        except User.DoesNotExist:
            return HttpResponseRedirect("/dashboard/users")
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def update_user(request, id):
    if check_auth_user_staff(request):
        if request.POST.get('cancel'):
            return HttpResponseRedirect("/dashboard/users")
        else:
            try:
                user = User.objects.get(id=id)
                user.first_name = request.POST.get('fname')
                user.last_name = request.POST.get('lname')
                user.username = request.POST.get('username')
                user.email = request.POST.get('email')
                user.save()
                return HttpResponseRedirect("/dashboard/users")

            except User.DoesNotExist:
                return HttpResponseRedirect("/dashboard/users")
    else:
        return HttpResponseRedirect("/")


@login_required(login_url="/login")
def delete_user(request, id):
    if check_auth_user_staff(request):
        try:
            user = User.objects.get(id=id)
            user.delete()
            return HttpResponseRedirect("/dashboard/users")

        except User.DoesNotExist:
            return HttpResponseRedirect("/dashboard/users")
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def lock_user(request, id):
    if check_auth_user_staff(request):
        try:
            user = User.objects.get(id=id)
            user.is_active = False
            user.save()
            return HttpResponseRedirect('/dashboard/users')
        except User.DoesNotExist:
            return HttpResponseRedirect('/dashboard/users')
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def unlock_user(request, id):
    if check_auth_user_staff(request):
        try:
            user = User.objects.get(id=id)
            user.is_active = True
            user.save()
            return HttpResponseRedirect('/dashboard/users')
        except User.DoesNotExist:
            return HttpResponseRedirect('/dashboard/users')
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def upgrade_user(request, id):
    if check_auth_user_staff(request):
        try:
            user = User.objects.get(id=id)
            user.is_staff = True
            user.save()
            return HttpResponseRedirect("/dashboard/users")
        except User.DoesNotExist:
            return HttpResponseRedirect('/dashboard/users')
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def downgrade_user(request, id):
    if check_auth_user_staff(request):
        try:
            user = User.objects.get(id=id)
            user.is_staff = False
            user.save()
            return HttpResponseRedirect("/dashboard/users")
        except User.DoesNotExist:
            return HttpResponseRedirect('/dashboard/users')
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def get_categories(request):
    if check_auth_user_staff(request):
        categories = Category.objects.all()
        main_content_var = "Categories"
        context = {'categories': categories,
                   'mainContentVar': main_content_var}
        return render(request, 'admin/categories/categories.html', context)
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def add_category(request):
    if check_auth_user_staff(request):
        if request.method == "POST":
            category_form = CreateCategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()
                return HttpResponseRedirect("/dashboard/categories")
        else:
            category_form = CreateCategoryForm()
            context = {'category_form': category_form}
            return render(request, 'admin/categories/createCategory.html', context)
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def delete_category(request, id):
    if check_auth_user_staff(request):
        try:
            category = Category.objects.get(id=id)
            category.delete()
            return HttpResponseRedirect("/dashboard/categories")
        except Category.DoesNotExist:
            return HttpResponseRedirect('/dashboard/categories')
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def edit_category(request, id):
    if check_auth_user_staff(request):
        try:
            category = Category.objects.get(id=id)
            if request.method == "POST":
                category_form = CreateCategoryForm(
                    request.POST, instance=category)
                if category_form.is_valid():
                    category_form.save()
                    return HttpResponseRedirect("/dashboard/categories")
            else:
                category_form = CreateCategoryForm(instance=category)
                context = {'category_form': category_form}
                return render(request, 'admin/categories/createCategory.html', context)
        except Category.DoesNotExist:
            return HttpResponseRedirect("/dashboard/categories")
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def get_posts(request):
    if check_auth_user_staff(request):
        posts = Post.objects.all()
        main_content_var = "Posts"
        context = {'posts': posts, 'mainContentVar': main_content_var}
        return render(request, 'admin/posts/postsList.html', context)
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def delete_post(request, id):
    if check_auth_user_staff(request):
        try:
            post = Post.objects.get(id=id)
            post.delete()
            return HttpResponseRedirect("/dashboard/posts")
        except Post.DoesNotExist:
            return HttpResponseRedirect('/dashboard/posts')
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def add_post(request):
    if check_auth_user_staff(request):
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
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def edit_post(request, id):
    post = Post.objects.get(id=id)

    if check_auth_user_staff(request):
        try:
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
        except Post.DoesNotExist:
            return HttpResponseRedirect('dashboard/posts')
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def add_tag(request):
    if check_auth_user_staff(request):
        if request.method == "POST":
            tag_form = CreateTagForm(request.POST)
            if tag_form.is_valid():
                tag_form.save()
                return HttpResponseRedirect("/dashboard/tags")
        else:
            tag_form = CreateTagForm()
            context = {'tag_form': tag_form}
            return render(request, 'admin/tags/createTag.html', context)
    else:
        return HttpResponseRedirect('/')


@login_required(login_url="/login")
def tags(request):
    if check_auth_user_staff(request):
        tags = Tag.objects.all()
        mainContentVar = "tags"
        context = {'tags': tags, 'mainContentVar': mainContentVar}
        return render(request, 'admin/tags/tags.html', context)
    else:
        return HttpResponseRedirect('/')
