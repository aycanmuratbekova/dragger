from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse

from .models import Post, Comment
from .forms import CommentForm


class BlogIndexView(TemplateView):
    template_name = "blog_index.html"

    def get_context_data(self, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return context


class CategoryView(TemplateView):
    template_name = "blog_category.html"

    def get_context_data(self, **kwargs):
        category = self.kwargs.get('category')
        posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
        context = {
            "category": category,
            "posts": posts
        }
        return context


class BlogDetailView(FormMixin, TemplateView):

    template_name = 'blog_detail.html'
    model = Post
    # form_class = CommentForm

    def get_context_data(self, **kwargs):

        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post)
        form = CommentForm()
        context = {
            "post": post,
            "comments": comments,
            "form": form,
        }
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        if self.request.method == 'POST':
            form = CommentForm(self.request.POST)
            if form.is_valid():
                comment = Comment(
                    author=form.cleaned_data["author"],
                    body=form.cleaned_data["body"],
                    post=post
                )
                comment.save()

        return self.render_to_response(context)


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

