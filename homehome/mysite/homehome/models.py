from django.db import models

from django.utils import timezone

class Task(models.Model):
    """本日のミッション"""
    title= models.CharField(max_length=200)
    contents = models.TextField('タスク内容', blank=True)
    point = models.IntegerField('点数', default=0)
    pub_date = models.DateField('date published',default=timezone.now)
    is_completed = models.IntegerField(default=0)
    def __str__(self):
        return self.comment
