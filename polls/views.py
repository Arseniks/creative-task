from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "pageaboutme.html"


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")