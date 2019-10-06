from django.test import TestCase
from django.forms import forms
from django.contrib.auth import get_user_model

from core.models import Activity
from users.forms import UserRegisterForm

from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class ActivityTestCase(TestCase):
	def test_register_valid_form(self):
		"""
		Test Form with data.
		"""
		data = {
			'username': 'henry009',
			'password1': 'W0rldToUR',
			'password2': 'W0rldToUR',
		}

		form = UserCreationForm(data=data)
		self.assertTrue(form.is_valid())

	def test_register_invalid_form(self):
		"""
		Test Form with no data.
		"""
		data = {
			'username': 'henry009',
			'password1': '',
			'password2': '',
		}

		form = UserCreationForm(data=data)
		self.assertFalse(form.is_valid())

	def test_password_validation(self):
		"""
		Password 1 == Password 2.
		"""
		data = {
			'username': 'henry009',
			'password1': 'W0rldToUR',
			'password2': 'W0rldToUR',
		}

		form = UserCreationForm(data=data)
		self.assertEqual(form.data['password1'], form.data['password2'])



