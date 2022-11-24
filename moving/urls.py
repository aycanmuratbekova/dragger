from django.urls import path
from .views import CardIndexView, IndexView

urlpatterns = [

    path("all/", CardIndexView.as_view(), name='card_index'),
    path("index/", IndexView.as_view(), name='index_view_card'),

]
