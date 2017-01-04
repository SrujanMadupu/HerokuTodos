from __future__ import unicode_literals
from django.urls import reverse
from django.db import models

# Create your models here.
class Todo(models.Model):
	task = models.CharField(max_length=120)
	created = models.DateTimeField(auto_now=False,auto_now_add=True)
	lastdate = models.DateField(auto_now=False,auto_now_add=False,help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	def __str__(self):
		return self.task

	def get_absolute_url(self):
		#return '/crud/%s' %(self.id)
		return reverse('CRUD:gtodos')


class todolist(models.Model):
	todo = models.ForeignKey(Todo,on_delete=models.CASCADE)
	subtask = models.CharField(max_length=200)
	length  = models.IntegerField(default=0)
	completed = models.BooleanField(default=False)
	def __str__(self):
		return self.subtask

	def get_absolute_url(self):
		return '/crud/%s' %(self.todo.id)
