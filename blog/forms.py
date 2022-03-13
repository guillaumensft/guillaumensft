from django.forms import ModelForm,  formsets, Form
from django import forms
from .models import Article


# baseform
class MyForm(Form):

    titre = forms.CharField(required=True, help_text='insérer votre titre',
                            widget=forms.TextInput(attrs={'form-control'}))
    excerpt = forms.CharField(required=True, help_text='insérer un extrait',
                              widget=forms.TextInput(attrs={'form-control'}))
    content = forms.CharField(required=True, help_text="insérer le contenu de l'article",
                              widget=forms.TextInput(attrs={'form-control'}))


# modelform
class MyModelForm(ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'excerpt', 'content']

