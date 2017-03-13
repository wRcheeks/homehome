from django.conf.urls import url
from . import views

urlpatterns = [
    # 書籍
    url(r'^$', views.task_list, name='task_list'),   # 一覧
    url(r'^add/$', views.task_edit, name='task_add'),  # 登録
    url(r'^mod/(?P<task_id>\d+)/$', views.task_edit, name='task_mod'),  # 修正
    url(r'^del/(?P<task_id>\d+)/$', views.task_del, name='task_del'),   # 削除
    url(r'^comp_edit/(?P<task_id>\d+)/$', views.comp_edit,name='task_comp_edit'),
]
