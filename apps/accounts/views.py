from django.http import HttpResponse, Http404
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth import login, logout, authenticate, forms
from django.shortcuts import render, redirect # inserted this line
from .forms import RegisterForm
#from .models import THE, NAMES, OF, MODELS

class Register(View):
	form = forms.UserCreationForm
	def get(self, request):
		context = {'form' : self.form()}
		return render(request, 'accounts/register.html', context)

	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts/success')
		else:
			context = {'form': form}
			return render(request, 'accounts/register.html', context)

class Success(View):
	def get(self, request):
		return render(request, 'accounts/success.html')

class Login(View):
	form = forms.AuthenticationForm
	def get(self, request):
		context = {'form' : self.form()}
		return render(request, 'accounts/login.html', context)

	def post(self, request):
		form = self.form(None, request.POST)
		context = {'form': form}
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/accounts/success')
			else:
				return render(request, 'accounts/login.html', context)
		else:
			return render(request, 'accounts/login.html', context)

class Logout(View):
	def get(self, request):
		logout(request)
		return redirect('/accounts/login')