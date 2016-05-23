from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import adoffice.urls
import packaging.urls
from . import views
from filebrowser.sites import site
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import patterns
from django.http import HttpResponse

urlpatterns = i18n_patterns(
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^thanks/$', views.SubscriberPage.as_view(), name='subscribed'),
    #url(r'^product/$', views.ProductPage.as_view(), name='product'),
    url(r'^katalog/', include(adoffice.urls, namespace='adoffice')),
    # url(r'^opakowania/', include(packaging.urls, namespace='packaging')),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^admin/filebrowser/', include(site.urls)),
    #url(r'^i18n/', include('django.conf.urls.i18n')),
)
#urlpatterns += patterns('', url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")))
#(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'))
# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

