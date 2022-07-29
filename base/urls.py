from django.urls import path
from . import views

urlpatterns = [
    path('', views.pageList, name='pages')
]