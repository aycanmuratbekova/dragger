# users/urls.py

from django.urls import include, re_path, path
from .views import dashboard, register
from django.contrib.auth import views as auth_views #import this

urlpatterns = [

    # path('password_reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'),
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"),
    #      name='password_reset_confirm'),
    # path('reset/done/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'),
    #      name='login'),

    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    re_path(r"^dashboard/", dashboard, name="dashboard"),
    re_path(r"^oauth/", include("social_django.urls")),
    re_path(r"^register/", register, name="register"),
]

