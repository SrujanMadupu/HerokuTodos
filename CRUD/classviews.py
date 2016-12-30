from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Todo,todolist
from django.urls import reverse,reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User



@method_decorator(login_required, name='dispatch')
class AllTodos(ListView):
	model = Todo
	template_name = 'CRUD/todos.html'
	context_object_name = 'todos'
	def dispatch(self,*args,**kwargs):
		return super(AllTodos,self).dispatch(*args,**kwargs)
	def get_queryset(self):
		return Todo.objects.all()



@method_decorator(login_required, name='dispatch')
class DetailTodolist(ListView):
	model = todolist
	template_name = 'CRUD/todolist.html'
	context_object_name = 'list'
	def dispatch(self,*args,**kwargs):
		return super(DetailTodolist,self).dispatch(*args,**kwargs)
	def get_queryset(self):
		return get_object_or_404(Todo,id=self.kwargs['pk'])
		#return obj.todolist_set.all()



@method_decorator(login_required, name='dispatch')
class Createtodo(CreateView):
	model = Todo
	fields = ["task","lastdate"]
	template_name = 'CRUD/form.html'
	def dispatch(self,*args,**kwargs):
		return super(Createtodo,self).dispatch(*args,**kwargs)


@method_decorator(login_required, name='dispatch')
class Createtodolist(CreateView):
	model = todolist
	fields = ["subtask","length","completed","todo"]
	template_name = 'CRUD/form.html'
	def dispatch(self,*args,**kwargs):
		return super(Createtodolist,self).dispatch(*args,**kwargs)

@method_decorator(login_required, name='dispatch')
class Updatetodo(UpdateView):
	model = Todo
	fields = ["task","lastdate"]
	template_name = 'CRUD/form.html'
	def dispatch(self,*args,**kwargs):
		return super(Updatetodo,self).dispatch(*args,**kwargs)


@method_decorator(login_required, name='dispatch')
class Updatetodolist(UpdateView):
	model = todolist
	fields = ["subtask","length","completed","todo"]
	template_name = 'CRUD/form.html'
	def dispatch(self,*args,**kwargs):
		return super(Updatetodolist,self).dispatch(*args,**kwargs)


@method_decorator(login_required, name='dispatch')
class Deletetodo(DeleteView):
	model = Todo
	template_name = 'CRUD/todo_delete.html'
	success_url = reverse_lazy('CRUD:gtodos')
	def dispatch(self,*args,**kwargs):
		return super(Deletetodo,self).dispatch(*args,**kwargs)

@method_decorator(login_required, name='dispatch')
class Deletetodolist(DeleteView):
	model = todolist
	template_name = 'CRUD/todo_delete.html'
	#success_url = reverse_lazy('CRUD:gtodos')
	def dispatch(self,*args,**kwargs):
		return super(Deletetodolist,self).dispatch(*args,**kwargs)
	def get_success_url(self):
		p = todolist.objects.filter(id=self.kwargs['pk'])
		return reverse('CRUD:gdetail',kwargs={'pk':p[0].todo.id})










