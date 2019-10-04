from django.test import TestCase
from django.contrib.auth import get_user_model

from core.models import Activity
from core.forms import ActivityForm

User = get_user_model()


class ActivityTestCase(TestCase):
	def test_valid_form(self):
		"""
		Test form with data.
		"""
		name = "Gym"
		description = "Body building exercise"
		address = "405 Broadway"
		longitude = 34500
		latitude = 20000

		# create user
		user = User.objects.create(username='tom', password='tom')
		user.save()

		host_id = User.objects.get(username=user).pk
		postal_code = "10001"
		group_max_limit = 3
		obj = Activity.objects.create(
								name = name,
								description = description,
								address = address,
								longitude = longitude,
								latitude = latitude,
								host_id = host_id,
								postal_code = postal_code,
								group_max_limit = group_max_limit

		)

		data = {
			'name':name, 
			'description':description, 
			'address':address,
			'longitude':longitude,
			'latitude':latitude,
			'host_id': host_id,
			'postal_code':postal_code,
			'group_max_limit':group_max_limit
		}

		# Make sure the data is accurate
		form = ActivityForm(data=data)								# ActivityForm(request.POST)
		self.assertTrue(form.is_valid())
		self.assertEqual(form.cleaned_data.get('name'), obj.name)
		self.assertNotEqual(form.cleaned_data.get('description'), "Citee Twitte")

	def test_invalid_form(self):
		"""
		Test Form with empty data.
		"""
		name = "Gym"
		description = " "											# Empty content
		address = "405 Broadway"
		longitude = 34500
		latitude = 20000

		# create user
		user = User.objects.create(username='tom', password='tom')
		user.save()

		host_id = User.objects.get(username=user).pk
		postal_code = "10001"
		group_max_limit = 3
		obj = Activity.objects.create(
								name = name,
								description = description,
								address = address,
								longitude = longitude,
								latitude = latitude,
								host_id = host_id,
								postal_code = postal_code,
								group_max_limit = group_max_limit

		)
		
		data = {
			'name':name, 
			'description':description, 
			'address':address,
			'longitude':longitude,
			'latitude':latitude,
			'host_id': host_id,
			'postal_code':postal_code,
			'group_max_limit':group_max_limit
		}

		form = ActivityForm(data=data)
		self.assertFalse(form.is_valid())
		self.assertTrue(form.errors)





