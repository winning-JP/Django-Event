from django import forms
from .models import Event, EventDateOption, Participant


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'status']


class EventDateOptionForm(forms.ModelForm):
    class Meta:
        model = EventDateOption
        fields = ['candidate_date']


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'date_option', 'availability']
