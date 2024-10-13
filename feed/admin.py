from django.contrib import admin
from feed.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'user')

admin.site.register(Task, TaskAdmin)
