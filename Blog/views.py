from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from posts.models import Post, Category, ForrbiddenWord
from .forms import createBadWordForm


# Create your views here.

# for testing
def index(request):
    return render(request,'layouts/dashboard/base.html')
    
    

    

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



