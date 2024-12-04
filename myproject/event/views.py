from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

def index(request):
    events = Event.objects.all()
    context = {
        'title': 'Event Home',
        'message': 'Welcome to the event page!',
        'events': events,
    }
    return render(request, 'event/index.html', context)

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_index')  # 名前付きURLにリダイレクト
    else:
        form = EventForm()
    return render(request, 'event/create.html', {'form': form})
