from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import DeskList, DeskDetailView, delete_desk, ChangeColumnNameView, CardDetailView, ChangeCardView,\
    AddUserView, add_this_user, remove_this_user, LastVisited
from .views import create_column, delete_column, edit_column
from .views import create_card, delete_card, edit_card
from .views import like_desk, dislike_desk, FavoriteDesks, ArchivedDesks, archive_desk, de_archive_desk
from .views import drop


urlpatterns = [

    path("desk-list/", DeskList.as_view(), name='desk_list'),
    path("desk/<int:pk>/", DeskDetailView.as_view(), name="desk_detail"),
    path("delete-desk/<int:pk>/", delete_desk, name="delete_desk"),
    path("create-column/<int:pk>/", create_column, name="create_column"),
    path("delete-column/<int:pk>/", delete_column, name="delete_column"),
    path("change-column-name/<int:pk>/", ChangeColumnNameView.as_view(), name="edit_column"),
    path("edit-column/<int:pk>/", edit_column, name="edit_column"),

    path("create-card/<int:pk>/", create_card, name="create_card"),
    path("card-detail/<int:pk>/", CardDetailView.as_view(), name="card_detail"),
    path("delete-card/<int:pk>/", delete_card, name="delete_card"),
    path("change-card/<int:pk>/", ChangeCardView.as_view(), name="edit_column"),
    path("edit-card/<int:pk>/", edit_card, name="edit_column"),

    path("add-user/<int:desk_id>/", AddUserView.as_view(), name="add_user"),
    path("add-this-user/<int:user_id>/<int:desk_id>/", add_this_user, name="add_this_user"),
    path("remove-this-user/<int:user_id>/<int:desk_id>/", remove_this_user, name="remove_this_user"),


    path("like-desk/<int:desk_id>/", like_desk, name="like_desk"),
    path("dislike-desk/<int:desk_id>/", dislike_desk, name="dislike_desk"),
    path("favorite-desks/", FavoriteDesks.as_view(), name="favorite_desks"),

    path("archive-desk/<int:desk_id>/", archive_desk, name="archive_desk"),
    path("de-archive-desk/<int:desk_id>/", de_archive_desk, name="de_archive_desk"),
    path("archived-desks/", ArchivedDesks.as_view(), name="archived_desks"),


    path("last-visited/", LastVisited.as_view(), name="last_visited"),



    path("card-place/", drop, name="drop"),




]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
