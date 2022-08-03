from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import NotesPage

# Create your views here.
class PageList(ListView):
    model = NotesPage
    context_object_name = 'pages'


class PageDetail(DetailView):
    model = NotesPage
    context_object_name = 'page'
    template_name = 'base/page.html'


class CreatePage(CreateView):
    model = NotesPage
    fields = '__all__'
    success_url = reverse_lazy('pages')

class UpdatePage(UpdateView):
    model = NotesPage
    fields = '__all__'
    success_url = reverse_lazy('pages')

class DeletePage(DeleteView):
    model = NotesPage
    context_object_name = 'page'
    success_url = reverse_lazy('pages')
