from django.urls import path,include
from . import views

#app_name = 'Timesheetapp'

urlpatterns = [
    path('login/', views.login),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index),
    
    path('Officemanagement/', views.Officemanagement),
    path('Officemanagement/keimachidei/',views.keimachidei),
    path('Officemanagement/keimachidei/detail_keimachidei',views.detail_keimachidei),
    path('Officemanagement/<int:id>/', views.detail_office),
    path('Officemanagement/<int:id>/detail_setteing',views.detail_setteing),
    path('Usermanagement',views.Usermanagement),
    
    path('Workmanagement/',views.todoapp),
    path('todo_post/', views.todo_post),
    path('delete/<int:task_id>',views.todo_delete),
    path('Workmanagement/', views.Workmanagement),
    path('result/', views.Timesheetapp),
    path('result_2/', views.Timesheetapp_2),
    path('Workmanagement/list', views.list),
    path('Workmanagement/list_2', views.list_2),
    path('Managerpage', views.Managerpage),
    path('Managerpage/<int:id>/', views.detail_Managerpage),
]