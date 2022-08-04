from django.urls import path
from .views import PageDetail, PageList, CreatePage, UpdatePage, DeletePage, UserLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name="register"),
    path('', PageList.as_view(), name='pages'),
    path('page/<int:pk>/', PageDetail.as_view(), name='page'),
    path('page-create/', CreatePage.as_view(), name='page-create'),
    path('page-update/<int:pk>/', UpdatePage.as_view(), name='page-update'),
    path('page-delete/<int:pk>/', DeletePage.as_view(), name='page-delete'),
]