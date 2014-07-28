from django.conf.urls import patterns, include, url
from django.conf.urls import handler404, handler500, handler403
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ucbc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #for now there is only one app:
    url( r'^admin/', include( admin.site.urls ) ),
    url( r'^', include( 'simple.urls', namespace = 'simple' ) ),

)

handler404 = 'simple.views.handler404'
handler403 = 'simple.views.handler403'
