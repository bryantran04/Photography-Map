from django.shortcuts import render, render_to_response
from .models import Post
import urllib.request   



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

def search(request):
    return render(request, 'photography/search.html')

def results(request):
    zipcode = request.POST.get('search')
    
    posts=Post.objects.filter(zipcode=int(zipcode))

    return render_to_response('photography/results.html', {'posts': posts})



def profile(request, location_id):
    profile=Post.objects.get(id=location_id)

    return render_to_response('photography/profile.html', {'profile': profile})
