from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.conf import settings
import json

from helper_functions import (
        get_entries, get_entry_names_with_file_names, get_entry_url, get_entries_ajax, get_entry_contents
    )


def test_test(request):
    return HttpResponse('It\'s alive!')

def test_broken(request):
    a = 0/0
    return HttpResponse('I am supposed to return a 500 error!!!')


## HTML views ##

def home(request):
    template = loader.get_template('blog/index.html')

    entry_contents = get_entry_contents()

    context_dict = {}

    if entry_contents:
        context_dict['entry'] = entry_contents

    context = RequestContext(request, context_dict)

    return HttpResponse(template.render(context))


def redirect_to_blog_home(request):
    return HttpResponseRedirect(reverse('blog.views.home'))


def entry(request, name):
    template = loader.get_template('blog/entry.html')

    entry_contents = get_entry_contents(name)

    context_dict = {}

    if entry_contents:
        context_dict['entry'] = entry_contents

    context = RequestContext(request, context_dict)

    return HttpResponse(template.render(context))


def archive(request):
    template = loader.get_template('blog/archive.html')

    entries = get_entries()

    context = RequestContext(request, {
        'entries': entries
                                       }
    )

    return HttpResponse(template.render(context))



## API ##
def archive_list(request):
    json_response = json.dumps({'entries': get_entries_ajax()})
    return HttpResponse(json_response, content_type='application/json')



def entry_url(request, name=''):
    if not name:
        return HttpResponse('No entry specified.')
    else:
        return HttpResponse(get_entry_url(entry))


