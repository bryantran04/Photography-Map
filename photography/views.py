from django.shortcuts import render

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