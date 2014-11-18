from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from aec import settings
from journals.views import ArticleYearArchiveView,ArticleMonthArchiveView
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
    url(r'^archives/archive/(?P<year>[0-9]{4})/$',ArticleYearArchiveView.as_view(),name='article_year_archive'),
    url(r'^archives/$','journals.views.newspaperarticles_index',name='archives'),
                       #url(r'^archive_index/$','journals.views.archive_index',name='archive_index'),
    url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[-\w]+)/$',ArticleMonthArchiveView.as_view(),name="archive_month"),
    url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',ArticleMonthArchiveView.as_view(month_format='%m'),name="archive_month_numeric"),
     url(r'^arch$','journals.views.index',name='arch')                  
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
