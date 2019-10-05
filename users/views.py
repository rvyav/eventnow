from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegisterForm


@login_required
def register(request):
	"""
	Register new user.
	"""
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')			
			form.save()
			# messages
			messages.success(request, f'Account created for {username}!')
			return redirect('core:activity_list')
	else:
		form = UserRegisterForm()

	context = {'form': form}
	return render(request, 'users/register.html', context)

