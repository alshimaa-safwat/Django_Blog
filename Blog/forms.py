from django import forms
from django.contrib.auth.models import User
<<<<<<< HEAD
from posts.models import Category, Post, ForbiddenWord
=======
from posts.models import Category, Post, ForbiddenWord, Tag
>>>>>>> 3d5916f02edcddc095993b500944be1be3f6c06d


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
<<<<<<< HEAD
        fields = ('title', 'body', 'author', 'thumbnail', 'category','tags')
=======
        fields = ('title', 'body', 'author', 'tags', 'thumbnail', 'category')
>>>>>>> 3d5916f02edcddc095993b500944be1be3f6c06d
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
<<<<<<< HEAD
            'tags':forms.Select(attrs={'class': 'form-control'})
=======
            'tags': forms.Select(attrs={'class': 'form-control'}),

>>>>>>> 3d5916f02edcddc095993b500944be1be3f6c06d
        }


class CreateBadWordForm(forms.ModelForm):
    class Meta:
        model = ForbiddenWord
        fields = ('word',)
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control'}),
        }
<<<<<<< HEAD
=======



class CreateTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
>>>>>>> 3d5916f02edcddc095993b500944be1be3f6c06d
