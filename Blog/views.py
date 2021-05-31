from django.shortcuts import render
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


