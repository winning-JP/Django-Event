from django.shortcuts import render, redirect
from .models import Event, EventDate
from .forms import EventForm, EventDateForm

def create_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        date_form = EventDateForm(request.POST)
        
        if event_form.is_valid() and date_form.is_valid():
            # STEP1: イベントを保存
            event = event_form.save()
            
            # STEP2: 日程候補を改行で分割し、日付と時間を保存
            date_times = date_form.cleaned_data['date_time_choices'].splitlines()
            for dt in date_times:
                date, time = parse_date_time(dt)
                EventDate.objects.create(event=event, date=date, time=time)
            
            return redirect('event_detail', event_id=event.id)
    else:
        event_form = EventForm()
        date_form = EventDateForm()
    
    return render(request, 'event/create_event.html', {
        'event_form': event_form,
        'date_form': date_form,
    })

def parse_date_time(input_str):
    # 日時の文字列解析ロジック。日時のフォーマットに応じて実装。
    from datetime import datetime
    # "8/7(月) 19:00〜" -> 日付と時間を分離
    parts = input_str.split(' ')
    date_part = parts[0]
    time_part = parts[1] if len(parts) > 1 else None

    # 日付解析
    date = datetime.strptime(date_part, "%m/%d").date()
    
    # 時間解析
    time = datetime.strptime(time_part, "%H:%M").time() if time_part else None
    return date, time
