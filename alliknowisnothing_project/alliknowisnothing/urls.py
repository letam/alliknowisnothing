from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alliknowisnothing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),

    # make ze home page redirect to ze blog
    url(r'^$', 'blog.views.redirect_to_blog_home'),

)
