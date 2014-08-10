from django.conf.urls import patterns, include, url
from django.conf.urls import handler404, handler500, handler403
from django.contrib import admin
from filebrowser.sites import site

#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/filebrowser/', include(site.urls)),
    url( r'^admin/', include( admin.site.urls ) ),
    url( r'^', include( 'simple.urls', namespace = 'simple' ) ),
)

#FIXME - DO I NEED THIS GUY?
#urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.MEDIA_URL + settings.FILEBROWSER_VERSIONS_BASEDIR, document_root=settings.MEDIA_ROOT )
#print settings.MEDIA_URL + settings.FILEBROWSER_VERSIONS_BASEDIR

handler404 = 'simple.views.handler404'
handler403 = 'simple.views.handler403'
