from django.conf import settings
from django.conf.urls import patterns, url, include, handler404, handler500
from django.conf.urls.static import static

#JEFFfrom django.contrib.flatpages import views as fviews

#JEFFfrom django.views.generic import TemplateView

from simple import views

urlpatterns = patterns('',
    #url( r'^int/$', views.staticViewJson, name="homePageView" ),
    #url( r'^int/(?P<category>news)/(?P<year>[\d]+)/(?P<slug>[\w\s-]+)/$', views.catPageViewJson, name="newsPostViewJason" ),
    #url( r'^int/(?P<category>ideas)/(?P<year>[\d]+)/(?P<slug>[\w\s-]+)/$', views.catPageViewJson, name="ideaViewJason" ),
    #url( r'^int/(?P<category>news)/$', views.listViewJson, name="newsViewJason" ),
    #url( r'^int/(?P<category>ideas)/$', views.listViewJson, name="ideasViewJason" ),
    #url( r'^int/(?P<slug>[\w\s-]+)/$', views.staticViewJson, name="pageViewJason" ),

    #for all my various pages WITHOUT json
    url( r'^$', views.staticView, name="homePageView" ),
    url( r'^(?P<category>news)/(?P<year>[\d]+)/(?P<slug>[\w\s-]+)/$', views.catPageView, name="newsPostView" ),
    url( r'^crew/(?P<pk>[\d]+)/$', views.crewView, name="crewView" ),
    url( r'^(?P<category>crews)/$', views.crewsView, name="crewsView" ),
    url( r'^(?P<category>news)/$', views.listView, name="newsView" ),
    url( r'^(?P<category>photos)/$', views.listView, name="photosView" ),
    url( r'^(?P<category>photos)/(?P<album>[\w\s-]+)/$', views.albumView, name="albumView" ),
    url( r'^(?P<slug>[\w\s-]+)/$', views.staticView, name="pageView" ),


    url( r'^submitContactForm$', views.submitContactForm, name="submitContactForm" ),
    #url( r'^submitKudos$', views.submitKudos, name="submitKudos" ),

    # UCBC static content view definitions
    #JEFFurl(r'^$', fviews.flatpage, {'url': '/'}, name='home'),
    #JEFFurl(r'^about/$', fviews.flatpage, {'url': '/about/'}, name='about'),
    #JEFFurl(r'^committee/$', fviews.flatpage, {'url': '/committee/'}, name='committee'),
    #JEFFurl(r'^contact/$', fviews.flatpage, {'url': '/contact/'}, name='contact'),
    #JEFFurl(r'^boats/$', fviews.flatpage, {'url': '/boats/'}, name='boats'),
    #JEFFurl(r'^boathouse/$', fviews.flatpage, {'url': '/boathouse/'}, name='boathouse'),
    #JEFFurl(r'^crews/$', fviews.flatpage, {'url': '/crews/'}, name='crews'),
    #JEFFurl(r'^news/$', fviews.flatpage, {'url': '/news/'}, name='news'),
    #JEFFurl(r'^get-involved/$', fviews.flatpage, {'url': '/get-involved/'}, name='get-involved'),
    #JEFFurl(r'^sponsors-alumni/$', fviews.flatpage, {'url': '/sponsors-alumni/'}, name='sponsors-alumni'),
    #JEFFurl(r'^gallery/$', fviews.flatpage, {'url': '/gallery/'}, name='gallery'),
    #url(r'^(?P<url>.*/)$', 'flatpage'), # Supposed to be a flatpage catch-all but doesn't seem to work...
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

