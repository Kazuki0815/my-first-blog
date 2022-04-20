from django import forms

from .models import Post

from blog.models import Timesheet,Kyoumachidei,employee,Offices

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        


class TimesheetForm(forms.ModelForm):

    class Meta:
        model = Timesheet
        fields = ('place', 'in_out')
        
class KyoumachideiForm(forms.ModelForm):
    class Meta:
        model = Kyoumachidei
        fields = ('shift_name', 'working_starttime','working_endtime','total_time','breakfast','lunch','dinner','office_id_test')
        
class employeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ('user', 'office_name','full_time','part_time','time','no_allowance_count')
        
class OfficesForm(forms.ModelForm):
    class Meta:
        model = Offices
        fields = ('office_name', 'office_manager')