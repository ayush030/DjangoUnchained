from django.urls import include, path
from . import views

app_name="cats"
urlpatterns=[
             path("", views.CatList.as_view(), name="catList"),
             path("main/create", views.CatCreate.as_view(), name="catCreate"),
             path("main/<int:pk>/update", views.CatUpdate.as_view(), name="catUpdate"),
             path("main/<int:pk>/delete", views.CatDelete.as_view(), name="catDelete"),
             
             path("lookup", views.BreedList.as_view(), name="breedList"),
             path("lookup/create", views.BreedCreate.as_view(), name="breedCreate"),
             path("lookup/<int:pk>/update", views.BreedUpdate.as_view(), name="breedUpdate"),
             path("lookup/<int:pk>/delete", views.BreedDelete.as_view(), name="breedDelete"),
            ]
