from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View

from autos.models import Autos, Make
# Create your views here.

class autosList(LoginRequiredMixin, View):
      def get(self, request):
    	  makeCount = Make.objects.all().count() #count of all objects in make model, refer autos.model.Make
    	  autosList = Autos.objects.all()         #all objects from autos.models.Autos
    	  
    	  context = {"makeCount": makeCount, "autosList":autosList}
    	  
    	  return render(request, "autos/autosList.html", context)


class autosCreate(LoginRequiredMixin, CreateView):
      model=Autos
      fields= "__all__"
      success_url= reverse_lazy("autos:autosList")

class autosEdit(LoginRequiredMixin, UpdateView):
      model = Autos
      fields = "__all__"
      success_url= reverse_lazy("autos:autosList")
    	  #return render(request, 'autos/autosedit.html')  --- not required as using generic class based views
    
    
class autosDelete(LoginRequiredMixin, DeleteView):
      model= Autos
      fields= "__all__"
      success_url= reverse_lazy("autos:autosList")
    	  #return render(request, 'autos/autosdelete.html')
    
# One just needs to specify which model to create Create View for and the fields. Then Class based CreateView will automatically try to find a template in app_name/modelname_form.html    

class makeList(LoginRequiredMixin, View):
      def get(self, request):
    	  makeList= Make.objects.all()
    	  context= {"makeList":makeList}
    	  
    	  return render(request, 'make/makeList.html', context)
    
    
class makeCreate(LoginRequiredMixin, CreateView):
      model= Make
      fields= "__all__"
      success_url= reverse_lazy("autos:autosList")
      	  
      	  
class makeEdit(LoginRequiredMixin, UpdateView):
      model= Make
      fields= "__all__"
      success_url= reverse_lazy("autos:autosList")
    	  #return render(request, 'make/makeedit.html')
    
    
class makeDelete(LoginRequiredMixin, DeleteView):    
      model= Make
      fields= "__all__"
      success_url= reverse_lazy("autos:autosList")
    	  #return render(request, 'make/makedelete.html')
    	  
    	  
    	  
#examples of views without using generic views

# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
#class MakeCreate(LoginRequiredMixin, View):
#    template = 'autos/make_form.html'
#    success_url = reverse_lazy('autos:all')

#    def get(self, request):
#        form = MakeForm()
#        ctx = {'form': form}
#        return render(request, self.template, ctx)

#    def post(self, request):
#        form = MakeForm(request.POST)
#        if not form.is_valid():
#            ctx = {'form': form}
#            return render(request, self.template, ctx)

#        make = form.save()
#        return redirect(self.success_url)


# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
#class MakeUpdate(LoginRequiredMixin, View):
 #   model = Make
 #   success_url = reverse_lazy('autos:all')
 #   template = 'autos/make_form.html'
#
 #   def get(self, request, pk):
 #       make = get_object_or_404(self.model, pk=pk)
 #       form = MakeForm(instance=make)
#        ctx = {'form': form}
 #       return render(request, self.template, ctx)
#
 #   def post(self, request, pk):
 #       make = get_object_or_404(self.model, pk=pk)
 #       form = MakeForm(request.POST, instance=make)
 #       if not form.is_valid():
 #           ctx = {'form': form}
 #           return render(request, self.template, ctx)
#
 #       form.save()
 #       return redirect(self.success_url)


#class MakeDelete(LoginRequiredMixin, View):
#    model = Make
#    success_url = reverse_lazy('autos:all')
#    template = 'autos/make_confirm_delete.html'
#
#   def get(self, request, pk):
#        make = get_object_or_404(self.model, pk=pk)
#        form = MakeForm(instance=make)
#        ctx = {'make': make}
#        return render(request, self.template, ctx)
#
#    def post(self, request, pk):
#        make = get_object_or_404(self.model, pk=pk)
#        make.delete()
#        return redirect(self.success_url)

