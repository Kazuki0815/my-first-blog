from django.contrib import admin
from .models import Post, Todo
from .models import Timesheet,Kyoumachidei,Offices,employee
#Profile
admin.site.register(Post)
admin.site.register(Todo)


admin.site.register(Timesheet)

#admin.site.register(Profile)
admin.site.register(employee)
admin.site.register(Offices)
admin.site.register(Kyoumachidei)