from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sites

#This class connect portfolio page with my works
#Displays all cards with sites on the page

class PortfolioPage(ListView):
    model = Sites
    template_name = 'main/portfolio.html'
    context_object_name = 'sites'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(PortfolioPage, self).get_context_data(**kwargs)
        ctx['title'] = 'Main page'
        return ctx

#This class сreates a separate page with information about the site 
    
class SiteDetail(DetailView):
    model = Sites
    template_name = 'main/sites-detail.html'

#This function connect main page with information about me 
    
def AboutMe(request):
    return render(request, 'main/me.html')

#This function connect contact page with my contact 

def Contact(request):
    return render(request, 'main/contacts.html')
