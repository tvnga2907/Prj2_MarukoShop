from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.", extra_tags='safe')
			return redirect('/')
		messages.error(request, "Unsuccessful registration. Invalid information.", extra_tags='safe')
	else:
		form = NewUserForm(	)
	return render (request=request, template_name="register.html", context={"form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.", extra_tags='safe')
				return redirect('/')
			else:
				messages.error(request,"Invalid username or password.", extra_tags='safe')
		else:
			messages.error(request,"Invalid username or password.", extra_tags='safe')
	else:
		form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.", extra_tags='safe')
	return redirect('/')