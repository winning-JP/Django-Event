from django.shortcuts import render


def index(request):
    context = {
        'title': 'Event Home',
        'message': 'Welcome to the event page!',
    }
    return render(request, 'event/index.html', context)
