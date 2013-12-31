from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alliknowisnothing.views.home', name='home'),

    url(r'^$', 'blog.views.home'),
    url(r'^archive/$', 'blog.views.archive'),
    url(r'^test/$', 'blog.views.test'),
    url(r'^broken/$', 'blog.views.broken'),

    url (r'^entry/(?P<entry>[\w-]+)/$', 'blog.views.get_entry_url'),
    url (r'^entry/$', 'blog.views.get_entry_url'),


)