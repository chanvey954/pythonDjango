from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('todos/', views.todos, name='Todos'),
    path('contact/', views.contact, name='Contact')
]
