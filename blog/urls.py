from django.urls import path
from . import views

urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('', views.index, name='index'),
    #path('post/Officemanagement/', views.Officemanagement, name='Officemanagement'),
    path('Officemanagement/', views.Officemanagement, name='Officemanagement'),
    path('Workmanagement/', views.Workmanagement, name='Workmanagement'),
    path('index/', views.index_2, name='index_2'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #http://127.0.0.1:8000/post/Officemanagement/
    #http://127.0.0.1:8000/post/Officemanagement.html
]