from django import forms
from .models import Todo,todolist

class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = [
            "task","lastdate"
		]

class TodoListForm(forms.ModelForm):
	class Meta:
		model = todolist
		fields = [
            "todo","subtask","length","completed"
		]