from django import forms
from .models import Event, EventDate

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'notes']

class EventDateForm(forms.Form):
    date_time_choices = forms.CharField(
        widget=forms.Textarea,
        help_text="日付と時間を改行で区切って入力します。例:\n8/7(月) 19:00〜\n8/8(火) 20:00〜"
    )
