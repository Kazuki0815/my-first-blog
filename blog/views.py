from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Offices,employee,Timesheet,Kyoumachidei
from .forms import KyoumachideiForm, TimesheetForm,employeeForm,OfficesForm
from datetime import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import  get_object_or_404

from django.urls import reverse
from urllib.parse import urlencode

#ログイン
def login(request):
    return render(request, 'five/index.html', {})

#ダッシュボード
def index(request):
    return render(request, 'blog/index/index.html', {})


#事業所管理
def office_list(request):
    offices = Offices.objects.all()#p
    context = {
        'offices': offices,
    }
    return render(request, 'blog/officemanagement/office_list.html',context)

def shift_details_page(request, id):
    shift_items = Kyoumachidei.objects.all()#p
    context = {
        'shift_items': shift_items,
        'id':id,
    }
    return render(request, 'blog/officemanagement/shift_details_page.html',context)

def shift_details_setteing(request,id):
    post = get_object_or_404(Kyoumachidei, pk=id)#p
    if request.method == "POST":
        form = KyoumachideiForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/Officemanagement/'+str(post.office_id_test_2.id)+'/shift_details_page')#p
    else:
        form = KyoumachideiForm(instance=post)#p
    context = {
        'form': form,
        'id':id,
    }
    return render(request, 'blog/officemanagement/shift_details_setteing.html',context)

def add_shift_item(request,id):
    if request.method == "POST":
        form = KyoumachideiForm(request.POST)#p
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/officemanagement/'+str(id)+'/shift_details_page')#p
    else:
        form = KyoumachideiForm()#p
    context = {
        'form': form,
        'id':id,
    }
    return render(request, 'blog/officemanagement/add_shift_item.html',context)

def delete_shift_item(request,id):
    delete_shift_item = Kyoumachidei.objects.get(pk=id)#p
    delete_shift_item.delete()
    return HttpResponseRedirect('/officemanagement/'+str(delete_shift_item.office_id_test_2.id)+'/shift_details_page')#p

def office_setting(request,id):    
    office = Offices.objects.all()#p
    post = get_object_or_404(Offices, pk=id)#p
    if request.method == "POST":
        form = OfficesForm(request.POST,instance=post)#p
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/officemanagement/office_list/')
    else:
        form = OfficesForm(instance=post)#p
    context = {
        'id':id,
        'office': office,
        'form':form,
    }
    return render(request, 'blog/officemanagement/office_setting.html',context)

#管理者管理
def manager_list(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'blog/managermanagement/manager_list.html',context)

#従業員管理
def employee_list(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'blog/usermanagement/employee_list.html',context)

def employee_details(request,id):#確認#Uersでまわし、requests.user.managerでとる
    #post = get_object_or_404(User, pk=id)
    post = User.objects.filter(manager__is_manager = 1,pk=id)
    #post = User.objects.filter(manager__is_manager = 1,pk=id)
    if request.method == "POST":
        form = employeeForm(request.POST,instance=post)#p
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/usermanagement/employee_list')
    else:
        form = employeeForm(request.POST)#p
        print("aa")
    context = {
        'id':id,
        'form':form,
    }
    return render(request, 'blog/usermanagement/employee_details.html',context)
    

#タイムカード
def timecard(request):
    #timesheet=  Timesheet.objects.get(pk=595)
    #if timesheet.leaving_work_time == None:
    #    context = {
    #        'ts':timesheet,
    #        'id':595,
    #    }
    #    return HttpResponseRedirect("/timecard/"+str(595)+"/",context)
    #tm = Timesheet.objects.filter(date=datetime.now().date())
    context = {
        #'tm': tm,
    }
    return render(request, 'blog/timecard/punch_in.html',context)

def timecard_in(request,id):
    context = {
        'id':id,
    }
    return render(request, 'blog/timecard/punch_out.html',context)

def attendance_stamp(request):
    #dbに追加
    ts = Timesheet()
    ts.staff = request.user
    office = Offices.objects.all()
    for offices in office:
        if offices == request.user.manager.office_name:
            workplace = offices
        else:
            print("例外")
    ts.office_name = workplace
    ts.date=datetime.now().date()
    ts.attendance_time=datetime.now().time()
    ts.save()
    
    context = {
        'ts':ts,
    }
    #return HttpResponseRedirect("/timecard/"+str(ts.id)+"/",context)
    return render(request, 'blog/timecard/punch_out.html', context)

    #return HttpResponseRedirect("/timecard/work_details/"+str(ts.id)+"/",context)
    #return HttpResponseRedirect("/timecard/work_details/{{ts.id}}/",context)

def leave_work_stamp(request,id):
    timesheet = Timesheet.objects.get(pk=id)
    if request.method == "POST":
        #post = request.POST.copy() # to make it mutable
        #post['shift_name'] = int(post['shift_name'])
        #request.POST = post
        #request.POST.shift_name = int(request.POST.shift_name)
        form = TimesheetForm(request.POST,instance=timesheet)
        #form.shift_name = int(form.shift_name)
        print( repr(request.POST) )
        if form.is_valid():
            timesheet = form.save(commit=False)
            timesheet.leaving_work_time=datetime.now().time()
            timesheet.save()
            #return redirect('/timecard/')
    else:
        form = TimesheetForm(instance=timesheet)
    context = {
        'form':form,
        'timesheet':timesheet,
        'id':'id',
    } 
    return HttpResponseRedirect("/timecard/work_details/"+str(id)+"/",context)
    #dbに追加
    #ts = Timesheet()
    #ts.staff = request.user
    ##ts.place="1"
    #office = Offices.objects.all()
    #for offices in office:
    #    if offices == request.user.manager.office_name:
    #        workplace = offices
    #    else:
    #        print("例外")
    #ts.office_name = workplace
    #ts.henkou="0"#
    #ts.time=datetime.now().time()
    #ts.date=datetime.now().date()
    #ts.attendance_time=datetime.now().time()
    #ts.leave_work_time=datetime.now().time()
    #ts.save()
    
    #画面に表示
    #now = datetime.now()
    #hour = now.hour
    #minute = now.minute
    
    #leave_work_time = str(hour) + ":" + str(minute)
    #context = {
    #    'leave_work_time': leave_work_time,
    #    'ts':ts,
    #}
    ##return HttpResponseRedirect("/timecard/work_details/"+str(timesheet.id)+"/",context)
    
    
    
    #return render(request, 'blog/timecard/work_details.html',context)


def work_details(request,id):
    timesheet = Timesheet.objects.get(pk=id)
    if request.method == "POST":
        post = request.POST.copy() # to make it mutable
        post['shift_name'] = int(post['shift_name'])
        request.POST = post
        #request.POST.shift_name = int(request.POST.shift_name)
        form = TimesheetForm(request.POST,instance=timesheet)
        #form.shift_name = int(form.shift_name)
        print( repr(request.POST) )
        if form.is_valid():
            timesheet = form.save(commit=False)
            timesheet.save()
            return redirect('/timecard/')
    else:
        form = TimesheetForm(instance=timesheet)
    context = {
        'form':form,
    } 
    return render(request, 'blog/timecard/work_details.html',context)

#勤務日誌個人
def this_month_work_diary(request):
    timesheets = Timesheet.objects.filter(staff=request.user)
    context = {
        'timesheets':timesheets,
    }
    return render(request, 'blog/personal_work_diary/this_month.html',context)

def next_month_work_diary(request):
    timesheets = Timesheet.objects.filter(staff=request.user)
    context = {
        'timesheets':timesheets,
    }
    return render(request, 'blog/personal_work_diary/next_month.html',context)


#勤務日誌管理者
def work_diary_list(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'blog/manager_work_diary/work_diary_list.html',context)

def work_diary_details(request,id):
    timesheets = Timesheet.objects.all()
    users = User.objects.all()
    context = {
        'users':users,
        'timesheets': timesheets,
        'id':id,
    }
    return render(request, 'blog/manager_work_diary/work_diary_details.html',context)


#削除予定
def Workmanagement(request):
    shift_item = Kyoumachidei.objects.all()
    return render(request, 'blog/Workmanagement.html', {'shift_item':shift_item})
#出勤打刻
def Timesheetapp(request):
    tm = Timesheet()
    tm.staff = request.user
    tm.henkou="1"
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
    }
    return render(request, 'blog/Workmanagement.html',context)

#退勤打刻
def Timesheetapp_2(request):
    tm = Timesheet()
    tm.staff = request.user
    tm.henkou="0"
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