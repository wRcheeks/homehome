from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm


def task_list(request):
    """タスクの一覧"""
    # return HttpResponse('書籍の一覧')
    tasks = Task.objects.all().order_by('pub_date')
    context = {
        'tasks' : tasks
    }
    return render(request,
                  'homehome/task_list.html',
                  context)         # テンプレートに渡すデータ

def task_edit(request, task_id=None):
    """タスクの編集"""
    if task_id:   # book_id が指定されている (修正時)
            task = get_object_or_404(Task, id=task_id)
    else:
            task = Task()

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            task = form.save(commit=False)
            task.save()
            return redirect('homehome:task_list')
    else:    # GET の時
        form = TaskForm(instance=task)  # book インスタンスからフォームを作成
        context = {
            'form' : form,
            'task_id':task_id
        }
        return render(request, 'homehome/task_edit.html', context)

def task_del(request, task_id):
    """書籍の削除"""
#     return HttpResponse('書籍の削除')
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('homehome:task_list')

def comp_edit(request, task_id):
    """可否の変更"""
    task = get_object_or_404(Task, id = task_id)
    if task.is_completed == 1:
        task.is_completed = 0
    else:
        task.is_completed = 1
    task.save()
    return redirect('homehome:task_list')
