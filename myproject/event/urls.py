from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='event_index'),
    path('create/', views.create_event, name='create_event'),
]
