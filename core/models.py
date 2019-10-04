from django.conf import settings
from django.db import models
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class Activity(models.Model):
	name = models.CharField(max_length=250, blank=False)
	description = models.TextField(max_length=1000)
	address = models.CharField(max_length=1000)
	longitude = models.CharField(max_length=1000)
	latitude = models.CharField(max_length=1000)
	postal_code = models.IntegerField()
	host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
	member = models.ManyToManyField(User, related_name='members')
	group_max_limit = models.SmallIntegerField()
	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created_at',)
		verbose_name_plural = 'activities'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('core:activity_detail', kwargs={'pk': self.pk })

class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comments')
	activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='activity_comments')
	body = models.TextField()
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return 'Comment by {} on {}'.format(self.author.username, self.activity.name)

