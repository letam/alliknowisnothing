from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader


def home(request):

    template = loader.get_template('blog/index.html')
    context = RequestContext(request, {
                                       }
    )

    return HttpResponse(template.render(context))


def redirect_to_blog_home(request):
    return HttpResponseRedirect(reverse('blog.views.home'))


def archive(request):

    return HttpResponse('The archive!')
