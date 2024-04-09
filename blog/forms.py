from .models import Comment, Contato
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