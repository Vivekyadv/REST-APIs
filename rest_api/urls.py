
from django.contrib import admin
from django.urls import path, include
from core.views import view, rest_view

urlpatterns = [
	path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('view/', view, name='view'),
    path('rest-view/', rest_view.as_view(), name='rest-view')

]
