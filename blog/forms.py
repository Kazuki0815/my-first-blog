from django import forms

from .models import Post

from blog.models import Timesheet

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        


class TimesheetForm(forms.ModelForm):

    class Meta:
        model = Timesheet
        fields = ('place', 'in_out')