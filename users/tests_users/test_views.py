from django.test import TestCase, Client
from django.urls import reverse

class TestUsersViews(TestCase):
	"""
	Test User Login & Registration Views.
	"""
	def setUp(self):
		self.client = Client()

	def test_login_get(self):
		"""
		Test Login page.
		"""
		response = self.client.get('/login/')

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/login.html')

	def test_login_post(self):
		"""
		Test Post request Login Views.
		"""
		data = {
			'username': 'tom', 
			'password': 'tom',
			'email': 'tom@gmail.com'
		}
		response = self.client.post('/login/', data)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/login.html')