from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'task')


admin.site.register(Task, TaskAdmin)
