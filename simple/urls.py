from django.conf import settings
from django.conf.urls import patterns, url, include, handler404, handler500
from django.conf.urls.static import static

from django.contrib.flatpages import views as fviews

from django.views.generic import TemplateView

from simple import views

urlpatterns = patterns('',
    #url( r'^int/$', views.staticViewJson, name="homePageView" ),
    #url( r'^int/(?P<category>news)/(?P<year>[\d]+)/(?P<slug>[\w\s-]+)/$', views.catPageViewJson, name="newsPostViewJason" ),
    #url( r'^int/(?P<category>ideas)/(?P<year>[\d]+)/(?P<slug>[\w\s-]+)/$', views.catPageViewJson, name="ideaViewJason" ),
    #url( r'^int/(?P<category>news)/$', views.listViewJson, name="newsViewJason" ),
    #url( r'^int/(?P<category>ideas)/$', views.listViewJson, name="ideasViewJason" ),
    #url( r'^int/(?P<slug>[\w\s-]+)/$', views.staticViewJson, name="pageViewJason" ),

    #for all my various pages WITHOUT json
    #url( r'^$', views.staticView, name="homePageView" ),
    #url( r'^(?P<category>news)/(?P<year>[\d]+)/(?P<slug>[\w\s-]+)/$', views.catPageView, name="newsPostView" ),
    #url( r'^(?P<category>ideas)/(?P<year>[\d]+)/(?P<slug>[\w\s-]+)/$', views.catPageView, name="ideaView" ),
    #url( r'^(?P<category>news)/$', views.listView, name="newsView" ),
    #url( r'^(?P<category>ideas)/$', views.listView, name="ideasView" ),
    #url( r'^(?P<slug>[\w\s-]+)/$', views.staticView, name="pageView" ),

    #url( r'^submitContactForm$', views.submitContactForm, name="submitContactForm" ),
    #url( r'^submitKudos$', views.submitKudos, name="submitKudos" ),

    # UCBC static content view definitions
    url(r'^$', fviews.flatpage, {'url': '/'}, name='home'),
    url(r'^about/$', fviews.flatpage, {'url': '/about/'}, name='about'), 
    url(r'^committee/$', fviews.flatpage, {'url': '/committee/'}, name='committee'),
    url(r'^contact/$', fviews.flatpage, {'url': '/contact/'}, name='contact'),
    url(r'^boats/$', fviews.flatpage, {'url': '/boats/'}, name='boats'), 
    url(r'^boathouse/$', fviews.flatpage, {'url': '/boathouse/'}, name='boathouse'), 
    url(r'^crews/$', fviews.flatpage, {'url': '/crews/'}, name='crews'), 
    url(r'^news/$', fviews.flatpage, {'url': '/news/'}, name='news'), 
    url(r'^get-involved/$', fviews.flatpage, {'url': '/get-involved/'}, name='get-involved'), 
    url(r'^sponsors-alumni/$', fviews.flatpage, {'url': '/sponsors-alumni/'}, name='sponsors-alumni'),
    url(r'^gallery/$', fviews.flatpage, {'url': '/gallery/'}, name='gallery'),
    #url(r'^(?P<url>.*/)$', 'flatpage'), # Supposed to be a flatpage catch-all but doesn't seem to work...
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

