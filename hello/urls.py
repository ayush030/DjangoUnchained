from .  import views

from django.urls import path

app_name='hello'

urlpatterns = [
	path('', views.myview, name='myview'),
]
