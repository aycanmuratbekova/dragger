from django.contrib import admin
from .models import Desk, Column, Card, Comment, Guest, Favorite, Archive, LastVisit


class CardInline(admin.TabularInline):
    model = Card
    max_num = 12
    min_num = 1
    extra = 0


class ColumnInline(admin.TabularInline):
    inlines = [CardInline, ]
    model = Column
    max_num = 12
    min_num = 1
    extra = 0


# @admin.register(Desk)
# class DeskAdmin(admin.ModelAdmin):
#     inlines = [ColumnInline, ]
#     list_display = ('name', 'image', 'creator')


@admin.register(Desk)
class DeskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'creator')


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desk']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'column']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'body', 'created_on', 'card']


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['guest_user', 'to_desk']


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['to_user', 'to_desk']


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = ['to_user', 'to_desk']


@admin.register(LastVisit)
class LastVisitAdmin(admin.ModelAdmin):
    list_display = ['to_user', 'to_desk', 'last_visit']

