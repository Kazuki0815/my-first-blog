from django.test import TestCase

# Create your tests here.
#    obj = form.save(commit=False)
#    obj.place = request.POST["place"]
#    obj.in_out = request.POST["in_out"]
#    obj.staff = request.user
#    obj.date = datetime.now().date()
#    obj.time = datetime.now().time()
#    obj.save()
#    if request.POST["in_out"] == '1':
#        comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "出勤確認しました。今日も頑張りましょう！"
#    else:
#        comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "退勤確認しました。お疲れ様でした(^-^)!"
#    context = {
#        'place': Timesheet.PLACES[int(obj.place)-1][1],
#        'comment': comment,
#    }
#    return render(request, 'blog/result.html', context)
#    return render(request, 'blog/result.html')
    
   
    #obj = form.save
    #obj.place = request.POST["place"]
    #obj.in_out = request.POST["in_out"]
    #obj.staff = request.user
    #obj.date = datetime.now().date()
    #obj.time = datetime.now().time()
    #obj.save()
    #Timesheet_items.staff
    #Timesheet_items.place
    #Timesheet_items.in_out
    #Timesheet_items.time
    #Timesheet_items.date
    #{% endfor %}
    #user_name = Timesheet.staff
    
    #return render(request, 'blog/result.html', context)
    #返信用
    
    #return render(request, 'blog/result.html',{'Timesheet_items':Timesheet_items})
    #return render(request, 'blog/result.html', context)
    #return render(request, 'blog/Workmanagement.html',{'Timesheet_items':Timesheet_items})
# Create your views here.
#class IndexView(LoginRequiredMixin, View):
#def get(request):#def get(request):
#    form = TimesheetForm
#    context = {
#        'form': form,
#        "user": request.user,
#    }
#    return render(request, 'blog/2index.html', context)
#index_3 = IndexView.as_view()

#class ResultView(View):
#def ResultView(request):
#    form = TimesheetForm(request.POST)
#    now = datetime.now()
#    month = now.month
#    day = now.day
#    hour = now.hour
#    minute = now.minute

#    obj = form.save(commit=False)
#    obj.place = request.POST["place"]
#    obj.in_out = request.POST["in_out"]
#    obj.staff = request.user
#    obj.date = datetime.now().date()x
#    obj.time = datetime.now().time()
#    obj.save()
#    if request.POST["in_out"] == '1':
#        comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "出勤確認しました。今日も頑張りましょう！"
#    else:
#        comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "退勤確認しました。お疲れ様でした(^-^)!"
#    context = {
#        'place': Timesheet.PLACES[int(obj.place)-1][1],
#        'comment': comment,
#    }
#    return render(request, 'blog/result.html', context)
#    return render(request, 'blog/result.html')
#result = ResultView.as_view()

#if request.method == "POST":
    #form = TimesheetForm(request.POST)
    #TimesheetForm.place = request.POST["place"]
    #TimesheetForm.in_out = request.POST["in_out"]
    #TimesheetForm.staff = request.user
    #TimesheetForm.date = datetime.now().date()
    #TimesheetForm.time = datetime.now().time()
    #form.save()
    #if form.is_valid():
        #form.save()
        
        #def like(request):
#    Fav = Favorite()
#    Fav.user = request.user
#    Fav.favorite = post
#    Fav.save()
    #Timesheet.objects.create(place="1", in_out="1", time=datetime.now().time(),date=datetime.now().date(),staff=request.user)
    #Timesheet.save()
    #Timesheet_items = Timesheet.objects.all()