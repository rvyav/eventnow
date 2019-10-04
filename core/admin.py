from django.contrib import admin
from .models import Activity, Comment

admin.site.register(Activity)
admin.site.register(Comment)


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
# 	list_display = ('author', 'group', 'created', 'active')


# admin.site.register(Vote)