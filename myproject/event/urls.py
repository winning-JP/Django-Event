from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='event_index'),
    path('create/', views.create_event, name='create_event'),
    path('<int:id>/', views.event_detail, name='event_detail'),
    path('<int:id>/edit/', views.edit_event, name='edit_event'),
    path('<int:id>/delete/', views.delete_event, name='delete_event'),
]
