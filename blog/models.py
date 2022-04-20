from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string

def create_id():
    return get_random_string(22)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Todo(models.Model):
    content = models.TextField()

class Timesheet(models.Model):
    class Meta:
        db_table = 'attendance'
        
    PLACES = (
        (1, '京町デイ'),
        (2, '日夏デイ'),
        (3, '甘呂デイ'),
        (4, 'ECC'),
        (5, 'わが家'),
    )
    IN_OUT = (
        (1, 'IN'),
        (0, 'OUT'),
    )
    staff = models.ForeignKey(get_user_model(), verbose_name="スタッフ", on_delete=models.CASCADE, default=None)
    place = models.IntegerField(verbose_name='出勤場所名', choices=PLACES, default=None)
    in_out = models.IntegerField(verbose_name='IN/OUT', choices=IN_OUT, default=None)
    time = models.TimeField(verbose_name="打刻時間")
    date = models.DateField(verbose_name='打刻日')
    
    #def __str__(self):
    #    return self.staff

class Offices(models.Model):
    office_name = models.CharField(verbose_name='事業所名',max_length=20, default='')
    office_manager = models.OneToOneField(User, on_delete=models.CASCADE,default=None,blank=True,null=True)
    
    def __str__(self):
        return self.office_name

class employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='氏名')
    time = models.DecimalField(verbose_name='時間',max_digits=5,decimal_places=2,default=0.00)
    full_time = models.BooleanField(verbose_name='常勤',default=False)
    part_time = models.BooleanField(verbose_name='非常勤',default=False)
    office_name = models.ForeignKey(Offices,on_delete=models.CASCADE,verbose_name='所属事務所',default=None)
    no_allowance_count = models.BooleanField(verbose_name='手当カウントしない',default=False)
    
    #def __str__(self):
    #    return self.user

@receiver(post_save, sender=User)
def create_user_employee(sender, instance, created, **kwargs):
    if created:
        employee.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_employee(sender, instance, **kwargs):
    instance.employee.save()


class Kyoumachidei(models.Model):
    OFFICE_ID_TEST = (
        (1, '京町デイ'),
        (2, '日夏デイ'),
        (3, '甘呂デイ'),
        (4, 'ECC'),
    )
    shift_name = models.CharField(verbose_name='名称',max_length=200)
    working_starttime = models.TimeField(verbose_name='開始時間',default='00:00')
    working_endtime = models.TimeField(verbose_name='終了時間',default='00:00')
    total_time = models.DecimalField(verbose_name='合計時間',max_digits=5,decimal_places=2)
    breakfast = models.BooleanField(verbose_name='朝食',default=False)
    lunch = models.BooleanField(verbose_name='昼食',default=False)
    dinner = models.BooleanField(verbose_name='夕食',default=False)
    #office_id = models.ForeignKey(Offices,on_delete=models.CASCADE,verbose_name='事務所名',default=None,blank=True,null=True)
    office_id_test = models.IntegerField(verbose_name='事務所名', choices=OFFICE_ID_TEST, default=None,blank=True,null=True)
    #office_id = models.CharField(verbose_name='事務所番号',max_length=200,default='')
    
    def __str__(self):
        return self.shift_name