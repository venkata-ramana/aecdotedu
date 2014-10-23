from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from aec import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'news_events.views.index',name='index'),
    url(r'^/about/(?P<abouts_id>[0-9]+)/$','about.views.detail', name='detail'),
    url(r'^about$','about.views.about',name='about'),
    
    url(r'^/academics/(?P<academics_id>[0-9]+)/$','academics.views.adetail', name='adetail'),
    url(r'^academics$','academics.views.academics',name='academics'),
    
    url(r'^/infrastructure/(?P<infrastructure_id>[0-9]+)/$','infrastructure.views.idetail', name='idetail'),
    url(r'^infrastructure$','infrastructure.views.infrastructure',name='infrastructure'),
    url(r'^allnews$','news_events.views.allnews',name='allnews'),
    url(r'^allevents$','news_events.views.allevents',name='allevents'),
                      
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
