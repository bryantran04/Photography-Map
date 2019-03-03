from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse('about page')

def browse(request):
    return HttpResponse('browse page')

def contact(request):
    return HttpResponse('contact page')

# Create your views here.
def index(request):
    """
    View for the about_page.html
    :param request:
    :return renders the request parameter, html template, and the context list:
    """
    context = {}
    template = 'photography/index.html'
    return render(request, template, context)