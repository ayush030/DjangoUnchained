from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from ads.models import Ad, Comment, Fav
from ads.owners import OwnerUpdateView, OwnerDeleteView #,OwnerListView, OwnerDetailView, OwnerCreateView
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from ads.forms import CreateForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse

from django.db.models import Q
from django.contrib.humanize.templatetags.humanize import naturaltime
# Create your views here.

class AdListView(ListView):
      model = Ad	#any model specified shoul have owner field
      #fields = ["title", "price", "text", "picture", "comments"]
      #success_url already defined in urls.py	
      template_name= "ads/ad_list.html" 	#for user defined template
      
      def get(self, request):
          ad_list = Ad.objects.all()
          favorites = list()
          if request.user.is_authenticated:
             #rows = [{'id': 2}, {'id': 4} ... ]  (A list of rows)
             rows = request.user.favorite_ads.values('id')
             #favorites = [2, 4, ...] using list comprehension
             favorites = [ row['id'] for row in rows ]
          
          #request.GET is a dictionary object that contains all the arguments recieved  by get method call. 2nd get is dict method(dict.get())   
          strval =  request.GET.get("search", False)	
          if strval :
            # Simple title-only search
            # objects = Post.objects.filter(title__contains=strval).select_related().order_by('-updated_at')[:10]

            # Multi-field search
            # If you need to execute more complex queries (for example, queries with OR statements), you can use Q objects.Q is an object used to encapsulate a collection of keyword arguments. These keyword arguments are specified as in “Field lookups” above.
            # example: __icontains for case-insensitive search
             query = Q(title__icontains=strval)
             query.add(Q(text__icontains=strval), Q.OR)
             ad_list = Ad.objects.filter(query).select_related().order_by('-updated_at')[:10]
          else :
             ad_list = Ad.objects.all().order_by('-updated_at')[:10]

         # Augment the ad_list
          for obj in ad_list:
              obj.natural_updated = naturaltime(obj.updated_at)
  
          ctx = {'ad_list' : ad_list, 'favorites': favorites, 'search': strval}
          
          return render(request, self.template_name, ctx)
          
#########################################################################################################################################################################################
# csrf exemption in class based views
# https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
        
    def post(self, request, pk) :
        print("Add PK",pk)
        t = get_object_or_404(Ad, id=pk)
        fav = Fav(user=request.user, ad=t)
        try:
            fav.save()  # In case of duplicate key
        except IntegrityError as e:
            pass
        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
       
    def post(self, request, pk) :
        print("Delete PK",pk)
        t = get_object_or_404(Ad, id=pk)
        try:
            fav = Fav.objects.get(user=request.user, ad=t).delete()
        except Fav.DoesNotExist as e:
            pass

        return HttpResponse()
#########################################################################################################################################################################################


class AdDetailView(DetailView):
      model = Ad	#any model specified shoul have owner field
      fields = ["title", "price", "text", "picture", "comments"]
      template_name = "ads/ad_detail.html"
      
      def get(self, request, pk) :
        x = Ad.objects.get(id=pk)
        comments = Comment.objects.filter(ad=x).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'ad' : x, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)
      

class AdCreateView(LoginRequiredMixin, CreateView):
      model = Ad	#any model specified should have owner field
      #fields = ["title", "price", "text", "picture", "comments"]
      template_name = "ads/ad_form.html"
      success_url = reverse_lazy("ads:all")

      def get(self, request, pk=None):
      	  form = CreateForm()
      	  ctx = {'form': form}
      	  return render(request, self.template_name, ctx)
      	  
      def post(self, request, pk=None):
          form = CreateForm(request.POST, request.FILES or None)
          
          if not form.is_valid():
             ctx= {'form': form}
             return render(request, self.template_name, ctx)
          
          #add owner to the model before saving
          ad = form.save(commit=False)
          ad.owner = self.request.user
          ad.save()
          # https://django-taggit.readthedocs.io/en/latest/forms.html#commit-false
          form.save_m2m()    # Add this for tagme
          
          return redirect(self.success_url)
          

class AdUpdateView(LoginRequiredMixin, UpdateView):
      model = Ad	#any model specified shoul have owner field
      #fields = ["title", "price", "text", "picture", "comments"]
      template_name = 'ads/ad_form.html'
      success_url = reverse_lazy('ads:all')

      def get(self, request, pk):
          ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
          form = CreateForm(instance=ad)
          ctx = {'form': form}
          return render(request, self.template_name, ctx)

      def post(self, request, pk=None):
          ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
          form = CreateForm(request.POST, request.FILES or None, instance=ad)

          if not form.is_valid():
             ctx = {'form': form}
             return render(request, self.template_name, ctx)

          ad = form.save(commit=False)
          ad.save()
          # https://django-taggit.readthedocs.io/en/latest/forms.html#commit-false
          form.save_m2m()    # Add this for tagme

          return redirect(self.success_url)

class AdDeleteView(LoginRequiredMixin, DeleteView):
      model = Ad	#any model specified shoul have owner field
      template_name = "ads/ad_confirm_delete.html"
      
def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response
    
    
class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, ad=f)
        comment.save()
        return redirect(reverse('ads:ad_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "ads/comment_delete.html"
    
    def get_success_url(self):
        ad = self.object.ad
        return reverse('ads:ad_detail', args=[ad.id])
      
