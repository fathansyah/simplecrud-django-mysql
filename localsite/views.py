from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum, Count
from .models import Uang
from .forms import UangForm, CreateUserForm

def index(request):
    return render(request, 'localsite/index.html')

@login_required(login_url='login')
def mainurl(request):
	uangs = Uang.objects.all()
	totalorder = uangs.count()

	totalsimpanan = uangs.aggregate(sum=Sum('simpanan'))['sum'] or 0.00

	context = {'totalorder':totalorder, 'uangs':uangs, 'totalsimpanan':totalsimpanan}

	return render(request, 'localsite/main.html', context)


def signup(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'localsite/signup.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('main')
			else:
				messages.info(request, 'Username dan Password salah .. !')

		context = {}
		return render(request, 'localsite/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def datasimpanan(request):
	form = UangForm()
	if request.method == "POST":
		form = UangForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('main')
		else:
			return redirect('tambahsimpanan')
	
	context = {'form':form}
	
	return render(request, 'localsite/inputdata.html', context)


 

	