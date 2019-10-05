from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserRegisterForm(UserCreationForm):
	"""
	Handle the User
	registration form input.
	"""
	email = forms.EmailField(label='Email address')
	first_name = forms.CharField(label='First name', required=False, help_text='Optional')
	last_name = forms.CharField(label='Last name', required=False, help_text='Optional')
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)


	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
		)

	def clean(self, *args, **kwargs):
		"""
		Validate UserRegisterForm.
		"""
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 != password2:
			raise forms.ValidationError("Passwords must match!")
		return super(UserRegisterForm, self).clean(*args, **kwargs)
