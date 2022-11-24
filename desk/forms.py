from django import forms
from .models import Desk, Column, Card, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]


class CreateDeskForm(forms.ModelForm):
    class Meta:
        model = Desk
        fields = ["name", "image"]


class CreateColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ["name"]


class CreateCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["name", "description", "deadline"]
