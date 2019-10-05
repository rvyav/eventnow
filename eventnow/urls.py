from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('core.urls', namespace='core')),
	path('register/', include('users.urls', namespace='register')),
	path('', include('django.contrib.auth.urls'))
    
]
