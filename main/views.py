from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import BooksModel
from .forms import CreateBookForm


class HomeView(ListView):
    # model = BooksModel
    # queryset = BooksModel.objects.all()
    template_name = 'main/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        q = self.request.GET.get('q')
        # qs = super().get_queryset()
        if q:
            qs = BooksModel.objects.all().filter(name__icontains=q)
        else:
            qs = BooksModel.objects.all()
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('q')
        if q:
            context['q'] = q
        return context


class CreateBookView(CreateView):
    model = BooksModel
    # success_url = 'home/'
    template_name = 'main/form.html'
    # fields = ['name', 'price']
    form_class = CreateBookForm

    def get_success_url(self):
        return reverse('home')


class UpdateBookView(UpdateView):
    model = BooksModel
    template_name = 'main/update.html'
    fields = ['name', 'price']
    # success_url = 'home/'

    def get_success_url(self):
        return reverse('create')


class BookDetailView(DetailView):
    model = BooksModel
    template_name = 'main/detail.html'
