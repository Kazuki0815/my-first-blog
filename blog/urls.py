import sys
from unittest import result
from django.urls import path,include
from . import views
#from todoapp.views import todoapp
#from .templates.timecard.views2 import ResultView as reviws
app_name = 'Timesheetapp'

urlpatterns = [
    
    #path('', views.post_list, name='post_list'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
    #path('post/Officemanagement/', views.Officemanagement, name='Officemanagement'),
    path('Officemanagement/', views.Officemanagement, name='Officemanagement'),
    #path('Workmanagement/',views.Timesheetapp),#仮
    path('Workmanagement/',views.todoapp),
    
    path('Workmanagement/', views.Workmanagement),#, name='Workmanagement'
    #path('index/', views.index_2, name='index_2'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    
    path('todo_post/', views.todo_post),
    path('delete/<int:task_id>',views.todo_delete),
    path('start_time/',views.start_time),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('result/', views.Timesheetapp),
    path('result_2/', views.Timesheetapp_2),
    #path('result/', views.ResultView),
    path('IndexView/', views.get),
    path('list/', views.list,name="list"),
    path('Officemanagement/keimachidei/',views.keimachidei),
    path('Officemanagement/keimachidei/detail_keimachidei',views.detail_keimachidei)
    
    #http://127.0.0.1:8000/post/Officemanagement/
    #http://127.0.0.1:8000/post/Officemanagement.html
    #http://127.0.0.1:8000/accounts/login/
]