from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sites

def me(request):
    return render(request, 'main/me.html')

class PortfolioPage(ListView):
    model = Sites
    template_name = 'main/portfolio.html'
    context_object_name = 'sites'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(PortfolioPage, self).get_context_data(**kwargs)
        ctx['title'] = 'Main page'
        return ctx

class SiteDetail(DetailView):
    model = Sites
    template_name = 'main/sites-detail.html'

def AboutMe(request):
    return render(request, 'main/me.html')

def Contact(request):
    return render(request, 'main/contacts.html')