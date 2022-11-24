from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from desk.models import Desk, Column, Card, Comment
from .forms import CommentForm, CardForm

User = get_user_model()


class LockedView(LoginRequiredMixin):
    login_url = "admin:login"


class BoardView(LockedView, generic.ListView):
    model = Desk
    context_object_name = 'boards'
    template_name = 'board/board_list.html'


class CreateBoardView(LockedView, generic.CreateView):
    model = Desk
    template_name = 'board/create_board.html'
    fields = ['title', 'background', 'members']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('board_list')


class BoardDetailView(LockedView, generic.DetailView):
    model = Desk
    context_object_name = 'board'
    template_name = 'board/board_detail.html'


class UpdateBoardView(LockedView, generic.UpdateView):
    model = Desk
    template_name = 'board/update_board.html'
    fields = '__all__'


class CardListView(LockedView, generic.ListView):
    model = Card
    template_name = 'card/card_list.html'
    context_object_name = 'cards'

    def get_queryset(self):
        self.board = get_object_or_404(Desk, **self.kwargs)
        return Card.objects.all().order_by('column')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board'] = self.board
        return context


class CardDetailView(LockedView, generic.FormView, generic.DetailView):
    model = Card
    context_object_name = 'card'
    template_name = 'card/card_detail.html'
    form_class = CommentForm
    success_url = '#'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(card=self.get_object()).order_by('-created_on')
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                text=form.cleaned_data['text'],
                card=self.get_object(),
                author=self.request.user
            )
            comment.save()

        return super().form_valid(form)


class CardCreateView(LockedView, generic.CreateView):
    model = Card
    fields = '__all__'
    template_name = 'card/card_create.html'
    context_object_name = 'card'
    success_url = reverse_lazy('card_list')


class CardUpdateView(LockedView, generic.UpdateView):
    model = Card
    form_class = CardForm
    success_url = reverse_lazy('card_list')
    template_name = 'card/card_update.html'


class CardDeleteView(LockedView, generic.DeleteView):
    model = Card
    success_url = 'card_list'
    template_name = 'card/card_delete.html'


class ColumnCreateView(LockedView, generic.CreateView):
    model = Column
    fields = '__all__'
    template_name = 'column_create.html'
    context_object_name = 'column'
    success_url = reverse_lazy('card_list')

