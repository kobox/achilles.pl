__author__ = 'ko'
from django.conf.urls import url
from . import views
from .models import Category

urlpatterns = [
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', views.CategoryDetail.as_view(model=Category), name='detail'),
    ]