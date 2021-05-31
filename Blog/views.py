from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from posts.models import Category,ForrbiddenWord
from .forms import createCategoryForm, createBadWordForm


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


# def get_posts(request):
#     posts = Post.objects.all()
#     main_content_var = "Posts"
#     context = {'posts': posts, 'mainContentVar': main_content_var}
#     return render(request, 'admin/content/postsList.html', context) 


# def delete_post(request, post_id):
#     post = Post.objects.get(id=post_id)
#     post.delete()
#     return HttpResponseRedirect("/ourBlog/posts")





def words(request):
    word = ForrbiddenWord.objects.all()
    mainContentVar = "Forbidden Words"
    context = {'word': word, 'mainContentVar': mainContentVar}
    return render(request, 'admin/content/wordsForbidden.html', context)


def delete_word(request, id):
    word = ForrbiddenWord.objects.get(id=id)
    word.delete()
    return HttpResponseRedirect("/ourBlog/words")


def add_word(request):
    if request.method == "POST":
        badWord_form = createBadWordForm(request.POST)
        if badWord_form.is_valid():
            badWord_form.save()
            return HttpResponseRedirect("/ourBlog/words")
    else:
        badWord_form = createBadWordForm()
        context = {'badWord_form': badWord_form}
        return render(request, 'admin/content/createBadWord.html', context)


def edit_word(request, id):
    word = ForrbiddenWord.objects.get(id=id)
    if request.method == "POST":
        badWord_form = createBadWordForm(request.POST, instance=word)
        if badWord_form.is_valid():
            badWord_form.save()
            return HttpResponseRedirect("/ourBlog/words")
    else:
        badWord_form = createBadWordForm(instance=word)
        context = {'badWord_form': badWord_form}
        return render(request, 'admin/content/createBadWord.html', context)











     

