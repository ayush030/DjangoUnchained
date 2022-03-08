from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myview(request):
    #query the exisiting visits of the session from server
    visits = request.session.get("num_visits", 0) + 1
    
    #update the session visits on the server 
    request.session["num_visits"] = visits
    
    #reponse to the client about visits
    response = HttpResponse('view count=' + str(visits))
    
    #setting the cookie
    response.set_cookie('dj4e_cookie', 'f9f38a01', max_age=1000)
        
    return response
     
