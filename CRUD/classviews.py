from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Todo,todolist
from django.urls import reverse,reverse_lazy
from django.shortcuts import get_object_or_404

class AllTodos(ListView):
	model = Todo
	template_name = 'CRUD/todos.html'
	context_object_name = 'todos'

class DetailTodolist(ListView):
	model = todolist
	template_name = 'CRUD/todolist.html'
	context_object_name = 'list'
	def get_queryset(self):
		return get_object_or_404(Todo,id=self.kwargs['pk'])
		#return obj.todolist_set.all()



class Createtodo(CreateView):
	model = Todo
	fields = ["task","lastdate"]
	template_name = 'CRUD/form.html'

class Createtodolist(CreateView):
	model = todolist
	fields = ["subtask","length","completed","todo"]
	template_name = 'CRUD/form.html'

class Updatetodo(UpdateView):
	model = Todo
	fields = ["task","lastdate"]
	template_name = 'CRUD/form.html'

class Updatetodolist(UpdateView):
	model = todolist
	fields = ["subtask","length","completed","todo"]
	template_name = 'CRUD/form.html'



class Deletetodo(DeleteView):
	model = Todo
	template_name = 'CRUD/todo_delete.html'
	success_url = reverse_lazy('CRUD:gtodos')

class Deletetodolist(DeleteView):
	model = todolist
	template_name = 'CRUD/todo_delete.html'
	#success_url = reverse_lazy('CRUD:gtodos')
	def get_success_url(self):
		p = todolist.objects.filter(id=self.kwargs['pk'])
		return reverse('CRUD:gdetail',kwargs={'pk':p[0].todo.id})










