from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save


#事業所
class Offices(models.Model):#1
    office_name = models.CharField(verbose_name='事業所名',max_length=20, default='')
    office_manager = models.OneToOneField(User, verbose_name='所属長',on_delete=models.CASCADE,default=None,blank=True,null=True)
    
    def __str__(self):
        return self.office_name


#従業員
class employee(models.Model):#2
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='氏名',related_name="manager")
    full_time = models.BooleanField(verbose_name='常勤',default=False)
    part_time = models.BooleanField(verbose_name='非常勤',default=False)
    time = models.DecimalField(verbose_name='時間',max_digits=5,decimal_places=2,default=0.00)#確認
    office_name = models.ForeignKey(Offices,on_delete=models.CASCADE,verbose_name='所属事業所',default=None)#3#p
    #belongs_office = models.ForeignKey(Offices,on_delete=models.CASCADE,verbose_name='所属事業所',default=None,blank=True,null=True)
    no_allowance_count = models.BooleanField(verbose_name='手当カウントしない',default=False)
    #+α
    is_manager = models.BooleanField(verbose_name='所属長',default=False)
    
    def __str__(self):
        return str(self.office_name)+" : "+str(self.user)

#@receiver(post_save, sender=User)
#def create_user_employee(sender, instance, created, **kwargs):#確認
#    if created:
#        employee.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_employee(sender, instance, **kwargs):#確認
    #instance.employee.save()
#    instance.manager.save()

#シフト
class Kyoumachidei(models.Model):#4
    shift_name = models.CharField(verbose_name='シフト名',max_length=200)
    working_starttime = models.TimeField(verbose_name='開始時間',default='00:00')#5
    working_endtime = models.TimeField(verbose_name='終了時間',default='00:00')#6
    total_time = models.DecimalField(verbose_name='合計時間',max_digits=5,decimal_places=2)
    breakfast = models.BooleanField(verbose_name='朝食',default=False)
    lunch = models.BooleanField(verbose_name='昼食',default=False)
    dinner = models.BooleanField(verbose_name='夕食',default=False)
    office_id_test_2 = models.ForeignKey(Offices,on_delete=models.CASCADE,verbose_name='事務所名',default=None,blank=True,null=True)#8#p
    
    def __str__(self):
        return str(self.office_id_test_2)+" : "+self.shift_name


#タイムカード
class Timesheet(models.Model):#9
    class Meta:
        db_table = 'attendance'
        
    staff = models.ForeignKey(get_user_model(), verbose_name="スタッフ", on_delete=models.CASCADE, default=None)
    office_name = models.ForeignKey(Offices,on_delete=models.CASCADE,verbose_name='事業所',default=None,blank=True,null=True)#office
    attendance_time = models.TimeField(verbose_name="出勤時間",default=None,blank=True,null=True)
    leaving_work_time = models.TimeField(verbose_name="退勤時間",default=None,blank=True,null=True)
    date = models.DateField(verbose_name='日付',default=None,blank=True,null=True)
    remarks = models.TextField(verbose_name='備考欄',default=None,blank=True,null=True)
    overtime_hours = models.DecimalField(verbose_name='残業時間',max_digits=5,decimal_places=2,default=None,blank=True,null=True)
    shift_name = models.ForeignKey(Kyoumachidei, verbose_name="シフト選択", on_delete=models.CASCADE, default=None,blank=True,null=True)#shift
    is_breakfast = models.BooleanField(verbose_name='朝食',default=False)
    is_lunch = models.BooleanField(verbose_name='昼食',default=False)
    is_dinner = models.BooleanField(verbose_name='夕食',default=False)
    total_working_hours = models.TimeField(verbose_name="合計勤務時間",default=None,blank=True,null=True)
    general_affairs_entry_field = models.TextField(verbose_name='総務記入欄',max_length=400,default=None,blank=True,null=True)
    remarks_time = models.TimeField(verbose_name="備考時間",default=None,blank=True,null=True)
        
    def __str__(self):
        return str(self.office_name)+" : "+str(self.staff)
    








#削除予定
from django.utils.crypto import get_random_string
def create_id():
    return get_random_string(22)