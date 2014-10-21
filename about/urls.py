from django.conf.urls import patterns, include, url
#from about.views.detail,menu import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
                       
    url(r'^$','about.views.about',name='about'),
    url(r'^(?P<abouts_id>[0-9]+/$)','about.views.detail', name='detail'),
)




#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += staticfiles_urlpatterns()
