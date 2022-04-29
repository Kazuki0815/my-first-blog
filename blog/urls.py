from django.urls import path,include
from . import views

urlpatterns = [
    
    #ログイン
    path('login/', views.login),
    path('accounts/', include('django.contrib.auth.urls')),
    
    #ダッシュボード
    path('', views.index),
    
    #事業所管理
    path('officemanagement/office_list/', views.office_list),
    path('officemanagement/<int:id>/shift_details_page', views.shift_details_page),
    path('officemanagement/<int:id>/shift_details_setteing', views.shift_details_setteing),
    path('officemanagement/<int:id>/add_shift_item',views.add_shift_item),
    path('officemanagement/<int:id>/delete_shift_item', views.delete_shift_item),
    path('officemanagement/<int:id>/office_setting',views.office_setting),
    
    #管理者管理
    path('managermanagement/manager_list',views.manager_list), 
    
    #従業員管理
    path('usermanagement/employee_list',views.employee_list),
    path('usermanagement/<int:id>/employee_details',views.employee_details),#p
    
    #タイムカード
    path('timecard/', views.timecard),
    path('timecard/attendance_stamp/', views.attendance_stamp),
    path('timecard/<int:id>/', views.timecard_in),
    path('timecard/leave_work_stamp/<int:id>/', views.leave_work_stamp),
    path('timecard/work_details/<int:id>/', views.work_details),
    
    #勤務日誌個人
    path('personal_work_diary/this_month',views.this_month_work_diary),
    path('personal_work_diary/next_month',views.next_month_work_diary),
    
    #勤務日誌管理者
    path('manager_work_diary/work_diary_list', views.work_diary_list),
    path('manager_work_diary/<int:id>/work_diary_details', views.work_diary_details),
    
    #削除予定
    path('Workmanagement/', views.Workmanagement),
    path('result/', views.Timesheetapp),
    path('result_2/', views.Timesheetapp_2),
    path('Workmanagement/list', views.list),
    path('Workmanagement/list_2', views.list_2),
]