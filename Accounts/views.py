from django.shortcuts import render,redirect
from django.http  import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth import (authenticate,get_user_model,login,logout)
# Create your views here.
from .forms import LoginForm,UserRegistrationForm

def login_view(request):
	print(request.user.is_authenticated())
	next = request.GET.get('next')
	title = "Login Form"
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		login(request,user)
		print(request.user.is_authenticated())
		if next:
			return redirect(next)
		return redirect("CRUD:gtodos")

	context = {
	  "form": form,
	  "title" : title,
	}
	return render(request,"Accounts/login_form.html",context)

def Register_view(request):
	print(request.user.is_authenticated())
	title = "Registration Form"
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		login(request,user)
		return redirect('CRUD:gtodos')

	context = {
	  "title" : title,
	  "form" : form,
	}
	return render(request,"Accounts/registration_form.html",context)

def Logout_view(request): 
	logout(request)
	return redirect('CRUD:gtodos')

