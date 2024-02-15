from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import chat_view

urlpatterns = [
    # path('', views.index, name='index'),
    path('', chat_view, name='chat'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
