from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from cats.models import Cat, Breed

class CatList(LoginRequiredMixin, View):
      def get(self, request):
          breedCount = Breed.objects.all().count()
          catList = Cat.objects.all()
          
          context = {"catList":catList, "breedCount": breedCount}
          
          return render(request, "cats/catsList.html", context)
        

class CatCreate(LoginRequiredMixin, CreateView):
      model= Cat
      fields = "__all__"
      success_url = reverse_lazy("cats:catList")


class CatUpdate(LoginRequiredMixin, UpdateView):
      model= Cat
      fields = "__all__"
      success_url = reverse_lazy("cats:catList")
      
      
class CatDelete(LoginRequiredMixin, DeleteView):
      model= Cat
      fields = "__all__"
      success_url = reverse_lazy("cats:catList")
      

class BreedList(LoginRequiredMixin, View):
      def get(self, request):
          breedList = Breed.objects.all()
          
          context = {"breedList":breedList}
          
          return render(request, "cats/breedList.html", context)
          

class BreedCreate(LoginRequiredMixin, CreateView):
      model = Breed
      fields = "__all__"	#list of field "names(string)" of model
      success_url= reverse_lazy("cats:catList")
      

class BreedUpdate(LoginRequiredMixin, UpdateView):
      model = Breed
      fields = "__all__"
      success_url= reverse_lazy("cats:catList")
      

class BreedDelete(LoginRequiredMixin, DeleteView):
      model = Breed
      fields = "__all__"
      success_url= reverse_lazy("cats:catList")

