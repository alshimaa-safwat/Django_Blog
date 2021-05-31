from django import forms
from django.contrib.auth.models import User
from posts.models import Category, ForrbiddenWord

class createCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }



class createBadWordForm(forms.ModelForm):
    class Meta:
        model = ForrbiddenWord
        fields = ('word',)
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control'}),
        }
