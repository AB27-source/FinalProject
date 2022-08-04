from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse, reverse_lazy

# importing login view
from django.contrib.auth.views import LoginView

# importing LoginRequiredMixin to prevent unauthorized users from viewing pages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login

# importing NotesPage model
from .models import NotesPage


# views for user authentication
class UserLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        # when pages deleted it reverts user to homepage
        return reverse_lazy('pages')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    # if user is already signed in it redirects the user
    redirect_authenticated_user = True
    success_url = reverse_lazy('pages')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('pages')
        return super(RegisterPage, self).get(*args, **kwargs)
    

# views for models
class PageList(LoginRequiredMixin, ListView):
    # referencing NotesPage model
    model = NotesPage
    context_object_name = 'pages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = context['pages'].filter(user=self.request.user)

        search = self.request.GET.get('search_for') or ''
        # searching for note name
        if search:
            context['pages'] = context['pages'].filter(title__icontains=search)
        
        context['search'] = search
        return context

class PageDetail(LoginRequiredMixin, DetailView):
    # referencing NotesPage model
    model = NotesPage
    context_object_name = 'page'
    template_name = 'base/page.html'

class CreatePage(LoginRequiredMixin, CreateView):
    # referencing NotesPage model
    model = NotesPage
    fields = ['title', 'body']
    # when page is created it reverts user to homepage
    success_url = reverse_lazy('pages')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePage, self).form_valid(form)

class UpdatePage(LoginRequiredMixin, UpdateView):
    # referencing NotesPage model
    model = NotesPage
    # accessing every field in model
    fields = ['title', 'body']
    # when page is updated it reverts user to homepage
    success_url = reverse_lazy('pages')

class DeletePage(LoginRequiredMixin, DeleteView):
    # referencing NotesPage model
    model = NotesPage
    context_object_name = 'page'
    # when pages deleted it reverts user to homepage
    success_url = reverse_lazy('pages')


