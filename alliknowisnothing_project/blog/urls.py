from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alliknowisnothing.views.home', name='home'),

    url(r'^$', 'blog.views.home'),
    url(r'^archive/$', 'blog.views.archive'),
    url(r'^TEST_test/$', 'blog.views.test_test'),
    url(r'^TEST_broken/$', 'blog.views.test_broken'),

    url(r'^(?P<name>[\w-]+)/$', 'blog.views.entry'),


    ## API ##
    url(r'^api/archive/$', 'blog.views.archive_list'),
    url(r'^api/entry_url/(?P<name>[\w-]+)/$', 'blog.views.entry_url'),
    url(r'^api/entry_url/$', 'blog.views.entry_url'),


)