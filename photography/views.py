from django.shortcuts import render

# Create your views here.
def index(request):
    """
    View for the index.html
    :param request:
    :return renders the request parameter, html template, and the context list:
    """
    context = {}
    template = 'photography/index.html'
    return render(request, template, context)

def about(request):
    """
    View for the about.html
    :param request:
    :return renders the request parameter, html template, and the context list:
    """
    context = {}
    template = 'photography/about.html'
    return render(request, template, context)

def explore(request):
    """
    View for the about.html
    :param request:
    :return renders the request parameter, html template, and the context list:
    """
    context = {}
    template = 'photography/explore.html'
    return render(request, template, context)

