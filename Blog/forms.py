from django import forms
from django.contrib.auth.models import User
from Posts.models import Category
from .forms import createCategoryForm

class createCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }