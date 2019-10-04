from django import forms
from .models import Activity, Comment


class ActivityForm(forms.ModelForm):
	class Meta:
		model = Activity
		fields = ('name', 
				'description',
				'address',
				'longitude',
				'latitude',
				'postal_code',
				'group_max_limit'
		)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)

