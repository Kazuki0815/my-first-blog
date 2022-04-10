from email import header
from sqlite3 import Time
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post, Todo
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
import datetime
from .models import Post, Timesheet

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Timesheet
from .forms import TimesheetForm
from datetime import datetime, time
from django.utils import timezone

#dt_now = datetime.datetime.now()
#from .models import Todo

# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#def post_new(request):
#    form = PostForm()
#    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def Officemanagement(request):
     return render(request, 'blog/Officemanagement.html', {})
 
#def index_2(request):
#     return render(request, 'blog/index.html', {})
 
def Workmanagement(request):
    return render(request, 'blog/Workmanagement.html', {})

def todoapp(request):
    todo_items = Todo.objects.all()
    return render(request, 'blog/Workmanagement.html',{'todo_items':todo_items})
#入力を保存
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

def login(request):
    return render(request, 'five/index.html', {})


# Create your views here.
#class IndexView(LoginRequiredMixin, View):
def get(self, request):
    form = TimesheetForm
    context = {
        'form': form,
        "user": request.user,
    }
    return render(request, 'blog/2index.html', context)
#index_2 = IndexView.as_view()

def Timesheetapp(request):
    tm = Timesheet()
    tm.staff = request.user
    tm.place="2"
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
    #if Timesheet.in_out == "0":#本当は１で下が逆
    #    comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "退勤確認しました。お疲れ様でした!"
    #else:
    #    comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "出勤確認しました。今日も頑張りましょう！"
    context = {
        'comment': comment,
        'place': Timesheet.place,
    }
    return render(request, 'blog/Workmanagement.html',context)

def Timesheetapp_2(request):
    tm = Timesheet()
    tm.staff = request.user
    tm.place="2"
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
    #if Timesheet.in_out == "0":#本当は１で下が逆
    #    comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "退勤確認しました。お疲れ様でした!"
    #else:
    #    comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "出勤確認しました。今日も頑張りましょう！"
    context = {
        'comment_2': comment,
        'place': Timesheet.place,
    }
    return render(request, 'blog/Workmanagement.html',context)

def list(request):
    data = Timesheet.objects.filter(staff=request.user)
    #data = Timesheet.objects.get(in_out="1")
    #data_2 = Timesheet()
    #if data_2.in_out == "0":
    #    di = "出勤"
    #else:
    #    di ="退勤"
    #docchi = Timesheet.objects.filter(staff=request.user)
    aa = data
    if "2" in aa:
        kocchi = "出勤"
    else:
        kocchi = "退勤"
    params = {'message': 'メンバーの一覧', 'data': data,'kocchi':kocchi}
    return render(request, 'blog/Workmanagement.html', params)
    #data = Timesheet()
    #ds = request.user
    #if data.in_out=="1":
    #    dio = "出勤"
    #else:
    #    dio = "退勤"
    #dt = ""
    #dt = data.time
    #params = {'message':'打刻一覧','data':data,'dio':dio, "ds":ds,"dt":dt}
   # return render(request,'blog/Workmanagement.html',params)

def start_time(request):
    #start_task = Timesheet(start = request.POST['start'])
    #start_task.save()
    #print("start_task:"+start_task)
    dt_now = datetime.datetime.now()
    #dt_now.save()
    #header = (dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
    print(dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
    print("開始")
    return HttpResponseRedirect('/Workmanagement/')


def keimachidei(request):
    return render(request, 'blog/keimachidei.html')

def detail_keimachidei(request):
    return render(request, 'blog/detail_keimachidei.html')