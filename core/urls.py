from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls import (
    handler404, 
    handler500
)

handler404 = 'service.views.custom_404'
handler500 = 'service.views.custom_500'

app_name = 'core'
urlpatterns = [
	path('', views.activity_list, name='activity_list'),	
	path('<int:id>/', views.activity_detail, name='activity_detail'),
	path('profile/<int:id>/', views.profile, name='profile'),
	path('create-activity/', views.create_activity, name='create_activity'),
]