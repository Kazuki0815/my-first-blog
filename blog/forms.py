from django import forms
from django.contrib.auth.models import User
from blog.models import Offices,employee,Kyoumachidei,Timesheet
        
class OfficesForm(forms.ModelForm):
    class Meta:
        model = Offices
        fields = ('office_name', 'office_manager') 
    
    def __init__(self, *args, **kwargs):
        super(OfficesForm, self).__init__(*args, **kwargs)
        self.fields['office_manager'] = forms.ChoiceField(
            choices=[(o.id, str(o)) for o in User.objects.filter(manager__is_manager = 1,manager__office_name_id = self.instance.id)]
        )


class employeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ('user', 'office_name','full_time','part_time','time','no_allowance_count')


class KyoumachideiForm(forms.ModelForm):
    class Meta:
        model = Kyoumachidei
        fields = ('shift_name', 'working_starttime','working_endtime','total_time','breakfast','lunch','dinner','office_id_test_2')


class TimesheetForm(forms.ModelForm):

    class Meta:
        model = Timesheet
        fields = ('attendance_time','leaving_work_time','date','remarks','shift_name','overtime_hours','total_working_hours')
          
    #def __init__(self, *args, **kwargs):
    #    super(TimesheetForm, self).__init__(*args, **kwargs)
    #    self.fields['shift_name'] = forms.TypedChoiceField(
    #        choices=[(o.id, str(o)) for o in Kyoumachidei.objects.filter(office_id_test_2_id = 1)], coerce=int)
            #forms.TypedChoiceField(choices=[(x, x) for x in range(1, 11)], coerce=int, help_text = 'Units: ')
            #choices=[(o.id, str(o)) for o in Kyoumachidei.objects.filter(office_id_test_2_id = request.user.employee.office_name.id)]
            #from urllib import request

class MealForm(forms.ModelForm):

    class Meta:
        model = Timesheet
        fields = ('is_breakfast','is_lunch','is_dinner')
        
        
class RecordForm(forms.ModelForm):
    class Meta:
        model = Timesheet
        fields = ('general_affairs_entry_field',)
        widgets = {
            'general_affairs_entry_field': forms.Textarea(attrs={'rows':1, 'cols':15}),
        }