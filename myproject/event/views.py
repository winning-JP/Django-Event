from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm, EventDateOptionForm, ParticipantForm


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
    date_options = event.date_options.all().order_by('candidate_date')
    # 候補日をスコア順に並べたい場合は並び替え:
    # sorted_date_options =
    # sorted(date_options, key=lambda x: x.get_score(), reverse=True)
    # ここでは単純に日付順で表示してもOK
    participants = event.participants.all()
    context = {
        'event': event,
        'date_options': date_options,
        'participants': participants,
    }
    return render(request, 'event/detail.html', context)


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


def add_date_option(request, id):
    # イベントに候補日を追加するビュー
    event = get_object_or_404(Event, id=id)
    if event.is_closed():
        # 締め切りの場合は追加不可
        return redirect('event_detail', id=event.id)
    if request.method == 'POST':
        form = EventDateOptionForm(request.POST)
        if form.is_valid():
            date_option = form.save(commit=False)
            date_option.event = event
            date_option.save()
            return redirect('event_detail', id=event.id)
    else:
        form = EventDateOptionForm()
    return render(
        request,
        'event/add_date_option.html',
        {
            'form': form,
            'event': event
        }
    )


def add_participant(request, id):
    # 公開イベントに参加者を追加するビュー
    event = get_object_or_404(Event, id=id)
    if not event.is_public() or event.is_closed():
        # 公開中かつ締め切りでないイベント以外は不可
        return redirect('event_detail', id=event.id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        # formのdate_optionはそのイベントに属するものを選ぶこと
        if form.is_valid():
            participant = form.save(commit=False)
            # イベントが異なるdate_optionの選択を防ぐ
            if participant.date_option.event_id != event.id:
                return redirect('event_detail', id=event.id)
            participant.event = event
            participant.save()
            return redirect('event_detail', id=event.id)
    else:
        form = ParticipantForm()
        # イベントに紐づく候補日のみ表示させるよう、フィールドをクエリセットで制限
        form.fields['date_option'].queryset = event.date_options.all()
    return render(
        request,
        'event/add_participant.html',
        {
            'form': form,
            'event': event
        }
    )


def close_event(request, id):
    # イベントを締め切りにするビュー
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.status = 'closed'
        event.save()
        return redirect('event_detail', id=event.id)
    return render(request, 'event/close_confirm.html', {'event': event})


def public_events(request):
    # 公開状態のイベントのみを取得
    events = Event.objects.filter(status='public')
    return render(request, 'event/public_events.html', {'events': events})
