from django import forms
from django.contrib.auth.models import User
from posts.models import Category, Post, ForbiddenWord


# new user form
class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'author', 'thumbnail', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),

        }


class CreateBadWordForm(forms.ModelForm):
    class Meta:
        model = ForbiddenWord
        fields = ('word',)
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control'}),
        }
