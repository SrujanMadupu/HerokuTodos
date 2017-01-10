from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Todo,todolist
from django.urls import reverse,reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import ContextMixin



@method_decorator(login_required, name='dispatch')
class AllTodos(ListView):
	model = Todo
	template_name = 'CRUD/todos.html'
	context_object_name = 'todos'
	def dispatch(self,*args,**kwargs):
		return super(AllTodos,self).dispatch(*args,**kwargs)
	def get_queryset(self):
		todo_list =  Todo.objects.all()
		paginator = Paginator(todo_list,9)
		page = self.request.GET.get('page')
		try:
			objs = paginator.page(page)
		except PageNotAnInteger:
			objs = paginator.page(1)
		except EmptyPage:
			objs = paginator.page(paginator.num_pages)
		return objs



@method_decorator(login_required, name='dispatch')
class DetailTodolist(ListView,ContextMixin):
	model = todolist
	template_name = 'CRUD/todolist.html'
	#context_object_name = 'list'
	def dispatch(self,*args,**kwargs):
		return super(DetailTodolist,self).dispatch(*args,**kwargs)
	def get_context_data(self, **kwargs):
		context = super(DetailTodolist, self).get_context_data(**kwargs)
		todo_obj = get_object_or_404(Todo,id=self.kwargs['pk'])
		todo_items = todo_obj.todolist_set.all()
		paginator = Paginator(todo_items,9)
		page = self.request.GET.get('page')
		try:
			objs = paginator.page(page)
		except PageNotAnInteger:
			objs = paginator.page(1)
		except EmptyPage:
			objs = paginator.page(paginator.num_pages)
		context['list'] = objs
		context['title'] = todo_obj.task
		return context



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










