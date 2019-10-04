from django.test import TestCase
from core.models import Activity, Comment
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class ActivityModelTest(TestCase):
	def setUp(self):
		"""
		Setup fixtures for
		Activity and Comment Model.
		"""
		self.user = User.objects.create(username='tom', password='tom')

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

		self.comment = Comment.objects.create(
					body="testing comments", 
					author=self.user, 
					activity=self.activity
		)


	def test_activity_description(self):
		"""
		Test Activity model description.
		"""
		self.assertEqual(self.activity.description, 'stay healthing challenging your body')

	def test_verbose_name_plural(self):
		"""
		Test verbose name plural.
		"""
		self.assertEqual(str(Activity._meta.verbose_name_plural), "activities")


	def test_activity_get_absolute_url(self):
		"""
		Canonical URL to detail page.
		"""
		response = self.client.post(reverse('core:activity_detail', kwargs={'id':self.activity.id}))
		self.assertEqual(response.status_code, 200)


	def test_comment_body(self):
		"""
		Test Comment model body.
		"""
		self.assertEqual(self.comment.body, 'testing comments')









