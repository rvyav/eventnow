from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'core'
urlpatterns = [
	path('', views.activity_list, name='activity_list'),	
	path('<int:id>/', views.activity_detail, name='activity_detail'),
	#path('create-activity/', views.create_activity, name='create_activity'),
]