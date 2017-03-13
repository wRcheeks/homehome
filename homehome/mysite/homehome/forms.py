from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    """タスクのフォーム"""
    class Meta:
        model = Task
        fields = ('title', 'contents', 'point','pub_date' )
