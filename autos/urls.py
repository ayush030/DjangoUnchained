from django.urls import path
from . import views

app_name='autos'
urlpatterns=[
	path('', views.autosList.as_view(), name='autosList'),
	path('main/create', views.autosCreate.as_view(), name='autosCreate'),
	path('main/<int:pk>/update', views.autosEdit.as_view(), name='autosEdit'),
	path('main/<int:pk>/delete', views.autosDelete.as_view(), name='autosDelete'),
	
	path('lookup', views.makeList.as_view(), name='makeList'),
	path('lookup/create', views.makeCreate.as_view(), name='makeCreate'),
	path('lookup/<int:pk>/update', views.makeEdit.as_view(), name='makeEdit'),
	path('lookup/<int:pk>/delete', views.makeDelete.as_view(), name='makeDelete'),
]
