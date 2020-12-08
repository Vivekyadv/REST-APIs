
from django.contrib import admin
from django.urls import path
from core.views import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view, name='view')
]
