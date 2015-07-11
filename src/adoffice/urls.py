__author__ = 'ko'
from django.conf.urls import url
from . import views
from .models import Category, Product

urlpatterns = [
    url(r'^([\w-]+)/(?P<slug>[\w-]+)/$', views.ProductDetailView.as_view(model=Product), name='product'),
    url(r'^(?P<slug>[\w-]+)/$', views.CategoryDetail.as_view(model=Category), name='detail'),
    ]