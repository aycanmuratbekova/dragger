from django.urls import path
from . import views
from .views import BlogIndexView, CategoryView, BlogDetailView

urlpatterns = [
    # path("", views.blog_index, name="blog_index"),
    # path("<int:pk>/", views.blog_detail, name="blog_detail"),
    # path("<category>/", views.blog_category, name="blog_category"),


    path("", BlogIndexView.as_view(), name='blog_index'),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("<category>/", CategoryView.as_view(), name="blog_category"),

]
