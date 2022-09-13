from django.urls import path
from . import views

urlpatterns = [
    path('', views.me, name="i_am"),
    path('portfolio', views.PortfolioPage.as_view(), name="portfolio"),
    path('portfolio/<slug>', views.SiteDetail.as_view(), name='site-detail'),
    path('/me', views.AboutMe, name='me'),
    path('/contacts', views.Contact, name='contact')
]
