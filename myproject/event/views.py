from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('event_index')
    else:
        form = EventForm()
    return render(request, 'event/create.html', {'form': form})

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'event/detail.html', {'event': event})

def edit_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', id=event.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'event/edit.html', {'form': form, 'event': event})

def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_index')
    return render(request, 'event/delete_confirm.html', {'event': event})
