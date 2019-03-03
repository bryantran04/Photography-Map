from django.shortcuts import render, render_to_response
from .models import Post,Comment,Picture
import urllib.request   



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


def search(request):
    return render(request, 'photography/search.html')

def results(request):
    zipcode = request.POST.get('search')
    
    posts=Post.objects.filter(zipcode=int(zipcode))

    return render_to_response('photography/results.html', {'posts': posts})



def profile(request, location_id):
    profile=Post.objects.get(id=location_id)

    comments = profile.comment_set.all()
    pictures = profile.picture_set.all()
    # comments=Post.objects.get()
    return render_to_response('photography/profile.html', {'profile': profile, 'comments':comments,'pictures':pictures})
    return render_to_response('photography/profile.html', {'profile': profile})

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

