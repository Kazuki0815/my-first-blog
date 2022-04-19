from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Offices, Post, Todo, Timesheet,Kyoumachidei,Offices
from .forms import KyoumachideiForm,employeeForm,OfficesForm
from datetime import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


#ログイン
def login(request):
    return render(request, 'five/index.html', {})

#ダッシュボード
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {})

#事業所管理
def Officemanagement(request):
    if request.method == "POST":
        form = OfficesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #return redirect('keimachidei')
    else:
        form = OfficesForm()
    
    offices = Offices.objects.all()
    context = {
        'offices': offices,
        'form': form,
    }
    return render(request, 'blog/Officemanagement.html',context)

#京町デイ
def keimachidei(request):
    shift_item = Kyoumachidei.objects.all()
    params = {'shift_item': shift_item,}
    return render(request, 'blog/office/keimachidei.html', params)

def detail_keimachidei(request):
    if request.method == "POST":
        form = KyoumachideiForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #return redirect('keimachidei')
    else:
        form = KyoumachideiForm()
    return render(request, 'blog/office/detail_keimachidei.html', {'form': form})

    #form = KyoumachideiForm()
    #return render(request, 'blog/detail_keimachidei.html', {'form': form})
    #return render(request, 'blog/detail_keimachidei.html')

#ユーザー管理
def Usermanagement(request):
    if request.method == "POST":
        form = employeeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #return redirect('keimachidei')
    else:
        form = employeeForm()
        
    users = User.objects.all()
    user_name = User.objects.values_list('username', flat=True)
    user_email = User.objects.values_list('email', flat=True)
    context = {
        'user_name': user_name,
        'user_email':user_email,
        'users':users,
        'form': form,
    }
    return render(request, 'blog/Usermanagement.html',context)

#勤務管理機能
def Workmanagement(request):
    return render(request, 'blog/Workmanagement.html', {})

#メモ機能
def todoapp(request):
    todo_items = Todo.objects.all()
    return render(request, 'blog/Workmanagement.html',{'todo_items':todo_items})

def todo_post(request):
    todo_task = Todo(content = request.POST['content'])
    todo_task.save()
    #click_time = Todo(created_date = request.POST['created_date'])
    #click_time.save()
    return HttpResponseRedirect('/Workmanagement/')

def todo_delete(request,task_id):
    delete_task = Todo.objects.get(id=task_id)
    delete_task.delete()
    return HttpResponseRedirect('/Workmanagement/')

#出勤打刻
def Timesheetapp(request):
    tm = Timesheet()
    tm.staff = request.user
    tm.place="1"
    tm.in_out="1"
    tm.time=datetime.now().time()
    tm.date=datetime.now().date()
    tm.save()
    
    #画面に表示
    now = datetime.now()
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    
    comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "出勤確認しました。今日も頑張りましょう！"
    context = {
        'comment': comment,
        'place': Timesheet.place,
    }
    return render(request, 'blog/Workmanagement.html',context)

#退勤打刻
def Timesheetapp_2(request):
    tm = Timesheet()
    tm.staff = request.user
    tm.place="1"
    tm.in_out="0"
    tm.time=datetime.now().time()
    tm.date=datetime.now().date()
    tm.save()
    
    #画面に表示
    now = datetime.now()
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    
    comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "退勤確認しました。お疲れ様でした!"
    context = {
        'comment_2': comment,
        'place': Timesheet.place,
    }
    return render(request, 'blog/Workmanagement.html',context)

#一覧表示
def list(request):
    data = Timesheet.objects.filter(staff=request.user)
    params = {'message': 'メンバーの一覧', 'data': data,}
    return render(request, 'blog/Workmanagement.html', params)

def list_2(request):
    data = Timesheet.objects.filter(staff=request.user)
    params = {'message': 'メンバーの一覧', 'data': data,}
    return render(request, 'blog/workrecord_list/list_2.html', params)

#管理者画面
def Managerpage(request):
    data = Timesheet.objects.all()
    users = User.objects.all()
    context = {
        'users':users,
        'data': data,
    }
    return render(request, 'blog/Managerpage.html',context)