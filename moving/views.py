from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse

from .models import Card, Category
from collections import defaultdict


class CardIndexView(TemplateView):
    template_name = "card_index.html"

    def get_context_data(self, **kwargs):

        dict_ = defaultdict()
        categories = Category.objects.all()
        for category in categories:
            cards = Card.objects.filter(category=category)

        context = {
                'data': dict(dict_)
            }

        return context


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        list_ = []
        dict_ = defaultdict()
        categories = Category.objects.all()
        for i, category in enumerate(categories):
            cards = Card.objects.filter(category=category)
            dict_[category.name] = [card.body for card in cards]

        context = {
                'data': dict(dict_)
            }

        return context


# class DeleteCategoryView(TemplateView):
#     template_name = "index.html"
#
#     def get_context_data(self, **kwargs):
#         list_ = []
#         dict_ = defaultdict()
#         categories = Category.objects.all()
#         for i, category in enumerate(categories):
#             cards = Card.objects.filter(category=category)
#             dict_[category.name] = [card.body for card in cards]
#
#         context = {
#                 'data': dict(dict_)
#             }
#
#         return context



# class CategoryView(TemplateView):
#     template_name = "blog_category.html"
#
#     def get_context_data(self, **kwargs):
#         category = self.kwargs.get('category')
#         posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
#         context = {
#             "category": category,
#             "posts": posts
#         }
#         return context





# def blog_index(request):
#     posts = Post.objects.all().order_by('-created_on')
#     context = {
#         "posts": posts,
#     }
#     return render(request, "blog_index.html", context)
#
#
# def blog_category(request, category):
#     posts = Post.objects.filter(
#         categories__name__contains=category
#     ).order_by(
#         '-created_on'
#     )
#     context = {
#         "category": category,
#         "posts": posts
#     }
#     return render(request, "blog_category.html", context)
#
#
# def blog_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     form = CommentForm()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = Comment(
#                 author=form.cleaned_data["author"],
#                 body=form.cleaned_data["body"],
#                 post=post
#             )
#             comment.save()
#
#     comments = Comment.objects.filter(post=post)
#     context = {
#         "post": post,
#         "comments": comments,
#         "form": form,
#     }
#     return render(request, "blog_detail.html", context)

