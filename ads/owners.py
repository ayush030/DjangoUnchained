from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerListView(ListView):
    """
    Sub-class the ListView to pass the request to the form.
    """


class OwnerDetailView(DetailView):
    """
    Sub-class the DetailView to pass the request to the form.
    """


class OwnerCreateView(LoginRequiredMixin, CreateView):
    """
    Sub-class of the CreateView to automatically pass the Request to the Form
    and add the owner to the saved object.
    """
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    
    def form_valid(self, form):
    # Saves the form instance, sets the current object for the view, and redirects to get_success_url().    
        print('form_valid called')
        object = form.save(commit=False)
        object.owner = self.request.user  #this field shall be checked for form validity 
        object.save()
        return super(OwnerCreateView, self).form_valid(form)

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    """
    Sub-class the UpdateView to pass the request to the form and limit the
    queryset to the requesting user.
    """

    def get_queryset(self):
        print('update get_queryset called')
        """ Limit a User to only modifying their own data. """
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)	
        #out of all the update queries, only queries in which the requesting user is owner are selected


class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    """
    Sub-class the DeleteView to restrict a User from deleting other
    user's data.
    """
    #get query set for deleteview from model of choice. Here qs is restricted to firlds where owner is    requested user only	
    def get_queryset(self):
        print('delete get_queryset called')
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)

# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.form_valid

# https://stackoverflow.com/questions/862522/django-populate-user-id-when-saving-a-model

# https://stackoverflow.com/a/15540149

# https://stackoverflow.com/questions/5531258/example-of-django-class-based-deleteview
