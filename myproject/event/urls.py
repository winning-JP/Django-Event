from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='event_index'),
    path('create/', views.create_event, name='create_event'),
    path('<int:id>/', views.event_detail, name='event_detail'),
    path('<int:id>/edit/', views.edit_event, name='edit_event'),
    path('<int:id>/delete/', views.delete_event, name='delete_event'),
    path('<int:id>/add_date_option/',
         views.add_date_option, name='add_date_option'),
    path('<int:id>/add_participant/',
         views.add_participant, name='add_participant'),
    path('<int:id>/close/', views.close_event, name='close_event'),
    path('public/', views.public_events, name='public_events'),
]
