from django.conf.urls import patterns, url
from simple import views
from django.conf.urls import handler404, handler500

urlpatterns = patterns('',
    url( r'^int/$', views.staticViewJson, name="homePageView" ),
    url( r'^int/(?P<category>news)/(?P<year>[\d]+)/(?P<slug>[\w\s-]+)/$', views.catPageViewJson, name="newsPostViewJason" ),
    url( r'^int/(?P<category>ideas)/(?P<year>[\d]+)/(?P<slug>[\w\s-]+)/$', views.catPageViewJson, name="ideaViewJason" ),
    url( r'^int/(?P<category>news)/$', views.listViewJson, name="newsViewJason" ),
    url( r'^int/(?P<category>ideas)/$', views.listViewJson, name="ideasViewJason" ),
    url( r'^int/(?P<slug>[\w\s-]+)/$', views.staticViewJson, name="pageViewJason" ),

    #for all my various pages WITHOUT json
    url( r'^$', views.staticView, name="homePageView" ),
    url( r'^(?P<category>news)/(?P<year>[\d]+)/(?P<slug>[\w\s-]+)/$', views.catPageView, name="newsPostView" ),
    url( r'^(?P<category>ideas)/(?P<year>[\d]+)/(?P<slug>[\w\s-]+)/$', views.catPageView, name="ideaView" ),
    url( r'^(?P<category>news)/$', views.listView, name="newsView" ),
    url( r'^(?P<category>ideas)/$', views.listView, name="ideasView" ),
    url( r'^(?P<slug>[\w\s-]+)/$', views.staticView, name="pageView" ),

    url( r'^submitContactForm$', views.submitContactForm, name="submitContactForm" ),
    url( r'^submitKudos$', views.submitKudos, name="submitKudos" ),
)

