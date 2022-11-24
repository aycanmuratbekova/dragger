import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormMixin, CreateView
from django.contrib.auth.models import User


from .forms import CreateDeskForm, CreateColumnForm, CreateCardForm, CommentForm
from .models import Desk, Column, Card, Guest, Comment, Favorite, Archive, LastVisit


class LockedView(LoginRequiredMixin):
    login_url = "dashboard"


class DeskList(LockedView, FormMixin, TemplateView):

    template_name = 'desk_index.html'
    model = Desk

    def get_context_data(self):
        usr = self.request.user
        desks = Desk.objects.filter(creator=usr)
        guest_desks = Guest.objects.filter(guest_user=usr)
        archived = Archive.objects.filter(to_user=usr)
        archived_desks = []
        for arch in archived:
            archived_desks.append(arch.to_desk)
        favorites = Favorite.objects.filter(to_user=usr)
        favorite_desks = []
        for favor in favorites:
            favorite_desks.append(favor.to_desk)
        form = CreateDeskForm

        context = {
            'desks': desks,
            'guest_desks': guest_desks,
            'form': form,
            'favorite_desks': favorite_desks,
            'archived_desks': archived_desks,
        }
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        usr = self.request.user
        if self.request.method == 'POST':
            form = CreateDeskForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                new_desk = Desk(
                    name=form.cleaned_data["name"],
                    image=form.cleaned_data["image"],
                    creator=usr,
                )
                new_desk.save()

        return self.render_to_response(context)


@login_required
def delete_desk(request, *args, **kwargs):
    pk = kwargs.get('pk')
    desk = Desk.objects.get(id=pk)
    desk.delete()
    return HttpResponseRedirect("/trello/desk/{id}/".format(id=desk.id))


class DeskDetailView(LockedView, TemplateView):

    template_name = 'desk_detail.html'

    def get_context_data(self, **kwargs):

        usr = self.request.user
        pk = self.kwargs.get('pk')
        desk = Desk.objects.get(id=pk)
        columns = Column.objects.filter(desk=desk)
        form_column = CreateColumnForm
        form_card = CreateCardForm

        desk_guests = Guest.objects.filter(to_desk=desk)

        visited = LastVisit.objects.filter(to_user=usr).filter(to_desk=desk)
        if visited:
            visit = LastVisit.objects.get(to_desk=desk)
            visit.last_visit = datetime.datetime.now()
            visit.save()
        else:
            visit = LastVisit(
                to_desk=desk,
                to_user=self.request.user,
                last_visit=datetime.datetime.now(),
            )
            visit.save()
        context = {
            'columns': columns,
            'desk': desk,
            'form_column': form_column,
            'form_card': form_card,
            'desk_guests': desk_guests,
        }
        return context


@login_required
def create_column(request, *args, **kwargs):

    pk = kwargs.get('pk')
    desk = Desk.objects.get(id=pk)
    if request.method == 'POST':
        form = CreateColumnForm(request.POST)
        if form.is_valid():
            new_column = Column(
                name=form.cleaned_data["name"],
                desk=desk,
            )
            new_column.save()
    return HttpResponseRedirect("/trello/desk/{id}/".format(id=desk.id))


@login_required
def delete_column(request, *args, **kwargs):
    pk = kwargs.get('pk')
    column = Column.objects.get(id=pk)
    desk = Desk.objects.get(columns=column)
    column.delete()
    return HttpResponseRedirect("/trello/desk/{id}/".format(id=desk.id))


@login_required
def delete_card(request, *args, **kwargs):
    pk = kwargs.get('pk')
    card = Card.objects.get(id=pk)
    desk = Desk.objects.get(columns=card.column)
    card.delete()
    return HttpResponseRedirect("/trello/desk/{id}/".format(id=desk.id))


class ChangeColumnNameView(LockedView, TemplateView):

    template_name = 'desk/edit_column.html'

    def get_context_data(self, **kwargs):

        pk = self.kwargs.get('pk')
        column = Column.objects.get(id=pk)
        desk = Desk.objects.get(columns=column)
        form_column = CreateColumnForm

        context = {
            'column': column,
            'desk': desk,
            'form_column': form_column
        }
        return context


class AddUserView(LockedView, TemplateView):

    template_name = 'desk/add_user.html'

    def get_context_data(self, **kwargs):

        desk_id = self.kwargs.get('desk_id')
        desk = Desk.objects.get(id=desk_id)
        guest_users = Guest.objects.filter(to_desk=desk)
        all_users = User.objects.exclude(id=desk.creator_id)
        gs = []
        for u in guest_users:
            gs.append(u.guest_user)

        context = {

            'desk': desk,
            'users': all_users,
            'guest_users': gs,
        }
        return context


@login_required
def add_this_user(request, *args, **kwargs):

    user_id = kwargs.get('user_id')
    desk_id = kwargs.get('desk_id')
    new_guest_to_desk = Guest(
        guest_user_id=user_id,
        to_desk_id=desk_id,
    )
    new_guest_to_desk.save()

    return HttpResponseRedirect("/trello/add-user/{id}/".format(id=desk_id))


@login_required
def remove_this_user(request, *args, **kwargs):

    user_id = kwargs.get('user_id')
    desk_id = kwargs.get('desk_id')
    guest_user = Guest.objects.filter(guest_user_id=user_id).filter(to_desk_id=desk_id)
    guest_user.delete()
    return HttpResponseRedirect("/trello/add-user/{id}/".format(id=desk_id))


@login_required
def edit_column(request, *args, **kwargs):
    pk = kwargs.get('pk')
    column = Column.objects.get(id=pk)
    desk = Desk.objects.get(columns=column)
    if request.method == 'POST':
        form = CreateColumnForm(request.POST)
        if form.is_valid():
            column.name = form.cleaned_data["name"]
            column.save()
    return HttpResponseRedirect("/trello/desk/{id}/".format(id=desk.id))


@login_required
def create_card(request, *args, **kwargs):

    pk = kwargs.get('pk')
    column = Column.objects.get(id=pk)
    desk = Desk.objects.get(columns=column)
    if request.method == 'POST':
        form = CreateCardForm(request.POST)
        if form.is_valid():
            new_card = Card(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                deadline=form.cleaned_data["deadline"],
                column=column,
            )
            new_card.save()
    return HttpResponseRedirect("/trello/desk/{id}/".format(id=desk.id))


class CardDetailView(LockedView, FormMixin, TemplateView):

    template_name = 'card/card_detail.html'

    def get_context_data(self, **kwargs):

        pk = self.kwargs.get('pk')
        card = Card.objects.get(pk=pk)
        comments = Comment.objects.filter(card=card)
        form = CommentForm
        print('\n\n\n', form, '\n\n\n')
        column = Column.objects.get(cards=card)
        desk = Desk.objects.get(columns=column)
        context = {
            "card": card,
            "desk": desk,
            "comments": comments,
            "form": form,
        }
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        card = Card.objects.get(pk=pk)
        if self.request.method == 'POST':
            form = CommentForm(self.request.POST)
            if form.is_valid():
                comment = Comment(
                    author=self.request.user,
                    body=form.cleaned_data["body"],
                    card=card
                )
                comment.save()
            else:
                print("\n\n\n Error \n\n\n")

        return self.render_to_response(context)


class ChangeCardView(LockedView, TemplateView):

    template_name = 'card/edit_card.html'

    def get_context_data(self, **kwargs):

        pk = self.kwargs.get('pk')
        card = Card.objects.get(id=pk)
        desk = Desk.objects.get(columns=card.column)
        form_card = CreateCardForm

        context = {
            'card': card,
            'desk': desk,
            'form_card': form_card
        }
        return context


@login_required
def edit_card(request, *args, **kwargs):
    pk = kwargs.get('pk')
    card = Card.objects.get(id=pk)
    desk = Desk.objects.get(columns=card.column)
    if request.method == 'POST':
        form = CreateCardForm(request.POST)
        if form.is_valid():
            card.name = form.cleaned_data["name"]
            card.description = form.cleaned_data["description"]
            card.deadline = form.cleaned_data["deadline"]
            card.save()
    return HttpResponseRedirect("/trello/desk/{id}/".format(id=desk.id))


@login_required
def drop(request, *args, **kwargs):

    if request.method == 'POST':
        card_id = kwargs.get('card_id')
        column_id = kwargs.get('column_id')

        card = Card.objects.get(id=card_id)
        card.column = Column.objects.get(id=column_id)
        card.save()
        desk = Desk.objects.get(columns=card.column)
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return HttpResponseRedirect("/trello/desk/{id}/".format(id=desk.id))


@login_required
def like_desk(request, desk_id):
    desk = Desk.objects.get(id=desk_id)
    favor = Favorite(
        to_desk=desk,
        to_user=request.user,
    )
    favor.save()
    return HttpResponseRedirect("/trello/desk-list/")


@login_required
def dislike_desk(request, desk_id):
    desk = Desk.objects.get(id=desk_id)
    favor = Favorite.objects.get(to_desk=desk)
    favor.delete()
    return HttpResponseRedirect("/trello/desk-list/")


class FavoriteDesks(LockedView, TemplateView):

    template_name = 'desk/favorite_desks.html'

    def get_context_data(self):
        fav_desks = Favorite.objects.filter(to_user=self.request.user)
        context = {
            'favorite_desks': fav_desks,
        }
        return context


@login_required
def archive_desk(request, desk_id):
    desk = Desk.objects.get(id=desk_id)
    arch = Archive(
        to_desk=desk,
        to_user=request.user,
    )
    arch.save()
    return HttpResponseRedirect("/trello/desk-list/")


@login_required
def de_archive_desk(request, desk_id):
    desk = Desk.objects.get(id=desk_id)
    arch = Archive.objects.get(to_desk=desk)
    arch.delete()
    return HttpResponseRedirect("/trello/desk-list/")


class ArchivedDesks(LockedView, TemplateView):

    template_name = 'desk/archived_desks.html'

    def get_context_data(self):
        arch_desks = Archive.objects.filter(to_user=self.request.user)
        context = {
            'archived_desks': arch_desks,
        }
        return context


class LastVisited(LockedView, TemplateView):

    template_name = 'desk/last_visited_desks.html'

    def get_context_data(self):
        last_visited_desks = LastVisit.objects.filter(to_user=self.request.user).order_by('-last_visit')[:10]
        # desks = []
        # for lst in last_visited_desks:
        #     desks.append(lst.to_desk)

        context = {
            'last_visited_desks': last_visited_desks,
        }
        return context

