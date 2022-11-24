from django import forms
from desk.models import Card


class BoardForm(forms.Form):
    title = forms.CharField(max_length=36)
    background = forms.ImageField()


class CommentForm(forms.Form):
    text = forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Leave a comment'
    })


class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = '__all__'


class SearchForm(forms.Form):
    text = forms.CharField(label='Search by product name', max_length=250)
