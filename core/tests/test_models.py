from django.test import TestCase
from core.models import Activity, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class ActivityModelTest(TestCase):
	def setUp(self):
		"""
		Setup fixtures to test
		Activity Model.
		"""
		user = User.objects.create(username='tom', password='tom')
		user.save()

		Activity.objects.create(
					name="cycling", 
					description="stay healthing challenging your body",
					host_id=User.objects.get(username=user).pk,
					#member = "Group 2",
					address="212 Broadway, New York, NY",
					longitude="-73.988243",
					latitude="40.736481",
					postal_code="10009",
					group_max_limit="12"
		)

	def test_create_activity_name(self, name="cycling"):
		"""
		Test create new Activity Model name.
		"""
		return Activity.objects.get(name=name)

	def test_verbose_name_plural(self):
		"""
		Test verbose name plural.
		"""
		self.assertEqual(str(Activity._meta.verbose_name_plural), "activities")

	# def test_get_absolute_url(self):
	# 	"""
	# 	Canonical URL.
	# 	"""

	# def test_activity_description(self):
	# 	cycling = Activity.objects.get(name="cycling")
	# 	self.assertEqual(cycling.description(), 'Good for your health and burning calories')
