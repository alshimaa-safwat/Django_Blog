from django import forms
from django.contrib.auth.models import User
from posts.models import Category,ForrbiddenWord



class createBadWordForm(forms.ModelForm):
    class Meta:
        model = ForrbiddenWord
        fields = ('word',)
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control'}),
        }
