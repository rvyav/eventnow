from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json, pdb
from django.contrib import messages
from .models import Activity, Comment
from .forms import ActivityForm, CommentForm


User = get_user_model()


def activity_list(request):
	"""
	Display list of active activities.
	"""
	links = Activity.objects.all()
	
	activities = [
        [l.id, l.name, l.description, l.latitude, l.longitude, i]
        for i, l in enumerate(Activity.objects.filter(active=True))
    ]

	context = {'activities': json.dumps(activities), 'links':links}
	return render(request, 'core/index.html', context)


@transaction.atomic
def activity_detail(request, id):	
	"""
	Current logged-in User can join group 
	through Add button or remove themselves 
	from the group through the Remove button.
	"""
	group_details = get_object_or_404(Activity, id=id)


	if 'join-group' in request.POST:
		# Curent logged-in User joins the group
		try:
			group_to_join = Activity.objects.get(id=id)

			# Number of user in group == max_limit
			numbers_users = group_to_join.member.count()
			group_max = group_to_join.group_max_limit

			if numbers_users != group_max:
				add_user_to_group = User.objects.get(username=request.user)
				result = group_to_join.member.add(add_user_to_group)
				# messages
				messages.success(request, 'You joined the Group successfully')
				return redirect('core:activity_list')

			else:
				# messages
				messages.error(request, 'Group Currently full. Try again later.')
		except:
			# Raise Error Validation 
			return redirect('core:activity_list')

	elif 'leave-group' in request.POST:
		# Curent logged-in User leaves the group.
		group_to_join = Activity.objects.get(id=id)
		remove_user_to_group = User.objects.get(username=request.user)

		# If current user == group_creator
		# and else
		if remove_user_to_group == group_to_join.host:
			# messages
			messages.error(request, 'You can not leave the group. Delete group first')
		else:
			result = group_to_join.member.remove(remove_user_to_group)
			# messages
			messages.success(request, 'You left the Group successfully')
			return redirect('core:activity_list')
			

	# Comments section
	# Current comments per object
	current_comments = Activity.objects.get(id=id)
	comments = current_comments.activity_comments.filter(active=True)

	# Active comments
	active_comments = Comment.objects.filter(active=True)

	if request.method == "POST":
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.activity = group_details
			new_comment.author = request.user
			new_comment.save()
			# Redirect to detail page
			return redirect('core:activity_detail', id=group_details.id)
	
	else:
		comment_form = CommentForm()

	context = {
			'comments': comments,
			'group_details': group_details,
			'active_comments':active_comments,
			'comment_form': comment_form
	}

	return render(request, 'core/detail.html', context)



