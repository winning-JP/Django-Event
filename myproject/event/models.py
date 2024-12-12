from django.db import models


class Event(models.Model):
    STATUS_CHOICES = (
        ('draft', '下書き'),
        ('public', '公開中'),
        ('closed', '締め切り'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_public(self):
        return self.status == 'public'

    def is_closed(self):
        return self.status == 'closed'


class EventDateOption(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='date_options')
    candidate_date = models.DateField()

    def __str__(self):
        return f"{self.event.name} - {self.candidate_date}"

    def get_participation_summary(self):
        # 各候補日ごとの参加状況を集計
        # availability: 'o' (参加), 'x' (不参加), 'd' (どちらでも)
        participants = self.participants.all()
        count_o = participants.filter(availability='o').count()
        count_x = participants.filter(availability='x').count()
        count_d = participants.filter(availability='d').count()
        return {
            'o': count_o,
            'x': count_x,
            'd': count_d,
        }

    def get_score(self):
        # 順位付けのためにスコア算出ロジックを定義（例：Oを2点、Dを1点、Xを0点）
        summary = self.get_participation_summary()
        score = summary['o'] * 2 + summary['d'] * 1
        return score


class Participant(models.Model):
    AVAILABILITY_CHOICES = (
        ('o', '◯'),
        ('x', '✕'),
        ('d', '△'),
    )

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='participants')
    name = models.CharField(max_length=255)
    date_option = models.ForeignKey(
        EventDateOption, on_delete=models.CASCADE, related_name='participants')
    availability = models.CharField(max_length=1, choices=AVAILABILITY_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.event.name} ({self.date_option.candidate_date} : {self.availability})"
