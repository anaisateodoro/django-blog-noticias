from .models import Comment, Contato, Autor, Post
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

class AnotherForm(forms.Form):
    bar = forms.CharField(widget=SummernoteInplaceWidget())

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

# Apply summernote to specific fields.

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('id', 'data')


class AutorForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Autor
        fields = ['nome', 'email', 'senha']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'slug', 'content']