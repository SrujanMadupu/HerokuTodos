from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import Todo,todolist
from .forms import TodoForm,TodoListForm
# Create your views here.

def todos(request):
	tasks = Todo.objects.all().order_by('created')
	context = {
	   'todos' : tasks,
	}
	return render(request,'CRUD/todos.html',context)

def todolists(request,pk):
	obj = get_object_or_404(Todo,id=pk)
	query_set = obj.todolist_set.all();
	context = {
	   'pk' : pk,
	   'title' : obj.task,
	   'list' : query_set,
	}
	return render(request,'CRUD/todolist.html',context)

def createtodo(request):
	form = TodoForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	   'form' : form,
	}
	return render(request,'CRUD/todo_create.html',context)

def createtask(request,pk):
	form = TodoListForm(request.POST or None)
	form.fields['todo'].id=pk
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(reverse('CRUD:list',args=(form.fields['todo'].id)))
	context = {
	   'form': form,
	}
	return render(request,'CRUD/todotask_create.html',context)
