from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import NotesPage

# views for user authentication
class UserLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        # when pages deleted it reverts user to homepage
        return reverse_lazy('pages')

# views for models
class PageList(LoginRequiredMixin, ListView):
    # referencing NotesPage model
    model = NotesPage
    context_object_name = 'pages'

class PageDetail(LoginRequiredMixin, DetailView):
    # referencing NotesPage model
    model = NotesPage
    context_object_name = 'page'
    template_name = 'base/page.html'

class CreatePage(LoginRequiredMixin, CreateView):
    # referencing NotesPage model
    model = NotesPage
    fields = '__all__'
    # when page is created it reverts user to homepage
    success_url = reverse_lazy('pages')

class UpdatePage(LoginRequiredMixin, UpdateView):
    # referencing NotesPage model
    model = NotesPage
    # accessing every field in model
    fields = '__all__'
    # when page is updated it reverts user to homepage
    success_url = reverse_lazy('pages')

class DeletePage(LoginRequiredMixin, DeleteView):
    # referencing NotesPage model
    model = NotesPage
    context_object_name = 'page'
    # when pages deleted it reverts user to homepage
    success_url = reverse_lazy('pages')


