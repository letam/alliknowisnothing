from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alliknowisnothing.views.home', name='home'),

    url(r'archive[/]?', 'blog.views.archive'),
    url(r'$', 'blog.views.home'),


)