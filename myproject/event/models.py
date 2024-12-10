from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=200, verbose_name="イベント名")
    notes = models.TextField(blank=True, verbose_name="メモ（任意）")

    def __str__(self):
        return self.event_name

class EventDate(models.Model):
    event = models.ForeignKey(Event, related_name='dates', on_delete=models.CASCADE)
    date = models.DateField(verbose_name="日付")
    time = models.TimeField(verbose_name="時刻", blank=True, null=True)  # 時刻は任意

    def __str__(self):
        return f"{self.date} {self.time if self.time else ''}"
