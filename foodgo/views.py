from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django import template
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse


class IndexView(generic.ListView):
    template_name = 'foodgo/index.html'

def index(request):
    template_name = 'foodgo/index.html'
    template = get_template(template_name)
    context = RequestContext(request)
    return HttpResponse(template.render(context))
