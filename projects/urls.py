from django.urls import path
from .views import ProjectIndexView, ProjectDetailView

urlpatterns = [
    # path("", project_index, name='project_index'),
    # path("<int:pk>/", project_detail, name='project_detail'),

    path("", ProjectIndexView.as_view(), name='project_index'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),

]
