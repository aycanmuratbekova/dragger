from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class Card(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    # created_on = models.DateTimeField(auto_now_add=True)
    # last_modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', related_name='cards', on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    card = models.ForeignKey('Card', related_name='comments', on_delete=models.CASCADE)
