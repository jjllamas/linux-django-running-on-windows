from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('apps.helloworld.views',
	url(r'^$','index_view',name='index_url'),
)
