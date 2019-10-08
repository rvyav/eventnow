from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from core.models import Activity


User = get_user_model()


class TestCoreViews(TestCase):
	"""
	Test User Login & Registration Views.
	"""
	def setUp(self):
		self.client = Client()
		self.list_url = reverse('core:activity_list')
		self.user = User.objects.create_user('tom', 'tom@gmail.com','tom')


	def test_activity_list_user_login(self):
		"""
		Test Activity List views
		with users login.
		"""
		# user must be login to pass.
		self.client.login(username='tom', password='tom')
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, 200)

	def test_activity_list_user_not_login(self):
		"""
		Test Activity List views
		with no users login.
		"""
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, 302)

	def test_activity_template_context(self):
		"""
		Text length of items
		inside context managers
		passed to templates.
		"""
		# user must be login to pass.
		self.client.login(username='tom', password='tom')
		self.activity = Activity.objects.create(
					name="cycling", 
					description="stay healthing challenging your body",
					host=self.user,
					address="212 Broadway, New York, NY",
					longitude="-73.988243",
					latitude="40.736481",
					postal_code="10001",
					group_max_limit="12"
		)

		self.activity = Activity.objects.create(
					name="cycling", 
					description="stay healthing challenging your body",
					host=self.user,
					address="212 Broadway, New York, NY",
					longitude="-73.988243",
					latitude="40.736481",
					postal_code="10001",
					group_max_limit="12"
		)

		response = self.client.get(self.list_url)
		self.assertEqual(len(response.context['links']), 2)
















