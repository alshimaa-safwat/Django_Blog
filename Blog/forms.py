from django import forms
from django.contrib.auth.models import User
from posts.models import Category

class createCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }