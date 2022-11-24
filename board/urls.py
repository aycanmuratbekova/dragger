from django.urls import path
from board import views


urlpatterns = [
    path('', views.BoardView.as_view(), name='board_list'),
    path('create_board/', views.CreateBoardView.as_view(), name='create_board'),
    path('card/', views.CardListView.as_view(), name='card_list'),
    path('card/create/', views.CardCreateView.as_view(), name='card_create'),
    path('card/create_column/', views.ColumnCreateView.as_view(), name='column_create'),
    path('card/<int:pk>/', views.CardDetailView.as_view(), name='card_detail'),
    path('card/update:<int:pk>/', views.CardUpdateView.as_view(), name='card_update'),
    path('card/delete_my_card:<int:pk>/', views.CardDeleteView.as_view(), name='card_delete'),
]
