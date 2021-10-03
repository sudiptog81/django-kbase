from django import forms
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE

from kbase.models import Article, Category


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name'
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'body',
            'categories'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': TinyMCE(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
