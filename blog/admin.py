from django.contrib import admin
from .models import Post, Timesheet
from .models import Todo

admin.site.register(Post)

admin.site.register(Todo)

admin.site.register(Timesheet)