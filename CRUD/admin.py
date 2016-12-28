from django.contrib import admin
from .models import Todo,todolist
# Register your models here.

class TodoModelAdmin(admin.ModelAdmin):
	list_display = ["task","created","lastdate"]
	class Meta:
		model = Todo

class TodoListModelAdmin(admin.ModelAdmin):
	list_display = ["subtask","length","completed"]
	class Meta:
		model = todolist



admin.site.register(Todo,TodoModelAdmin)
admin.site.register(todolist,TodoListModelAdmin)
