from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.conf import settings
import json

from helper_functions import get_blog_entries, get_blog_entry_names_with_file_names

def home(request):

    template = loader.get_template('blog/index.html')
    context = RequestContext(request, {
                                       }
    )

    return HttpResponse(template.render(context))


def redirect_to_blog_home(request):
    return HttpResponseRedirect(reverse('blog.views.home'))


def archive(request):
    json_response = json.dumps({'entries': get_blog_entries()})
    return HttpResponse(json_response, content_type='application/json')


def get_entry_url(request, entry=''):
    if not entry:
        return HttpResponse('No entry specified.')
    else:
        entry = entry.lower()
        entries = get_blog_entry_names_with_file_names()
        if entry in entries:
            file_name = entries[entry]
            return HttpResponse(settings.BLOG_ENTRIES_URL + file_name)
        else:
            return HttpResponse()


def test(request):
    return HttpResponse('It\'s alive!')


def broken(request):
    a = 0/0
    return HttpResponse('I am supposed to return a 500 error!!!')

