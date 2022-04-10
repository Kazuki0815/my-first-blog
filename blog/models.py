from importlib.resources import contents
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


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
    #created_date = models.DateTimeField(default=timezone.now)
    #click_time = models.DateTimeField(default=timezone.now)

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