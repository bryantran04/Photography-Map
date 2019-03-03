from django.shortcuts import render, render_to_response
from .models import Post,Comment,Picture
from urllib import request, parse
import json



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


def api(comments):
    pos_list = [("None",0.0)]
    neg_list = [("None",0.0)]
    neu_list = [("None",0.0)]
    for comment in comments:
        data = parse.urlencode({"text":comment.choice_text}).encode()
        req =  request.Request("http://text-processing.com/api/sentiment/", data=data) # this will make the method "POST"
        resp = request.urlopen(req)
        response_text = resp.read()
        decoded = response_text.decode("utf-8")
        json_acceptable_string = decoded.replace("'", "\"")
        d = json.loads(json_acceptable_string)
        pos = float(d['probability']['pos'])
        neg = float(d['probability']['neg'])
        neu = float(d['probability']['neg'])


        if (d["label"]=='pos'):
            pos_list.append((comment.choice_text,pos))
        elif (d['label']=='neg'):
            neg_list.append((comment.choice_text,neg))
        else:
            neu_list.append((comment.choice_text,neu))
    pos_list.sort(key=lambda x: x[1], reverse=True)#sort the list by the value
    neg_list.sort(key=lambda x: x[1], reverse=True)#sort the list by the value
    neu_list.sort(key=lambda x: x[1], reverse=True)#sort the list by the value

    return pos_list,neg_list,neu_list

def profile(request, location_id):
    profile=Post.objects.get(id=location_id)

    comments = profile.comment_set.all()
    pictures = profile.picture_set.all()

    (pos_list,neg_list,neu_list) = api(comments)
 
    # comments=Post.objects.get()
    return render_to_response('photography/profile.html', {'profile': profile, 'comments':comments,'pictures':pictures,\
        'pos':pos_list[0][0],'neg':neg_list[0][0],'neu':neu_list[0][0]})

def about(request):
    context = {}
    template = 'photography/about.html'
    return render(request, template, context)

def create(request):
    if request.method == "POST":
        new_location = request.POST.get('location')
        new_caption = request.POST.get('description')
        new_zipcode = request.POST.get('zipcode')
        new_date = request.POST.get('date_posted')
        new_author = request.POST.get('author')
        Post.objects.create(location = new_location, description = new_caption, zipcode = new_zipcode, date_posted = new_date, author = new_author)
    context = {}
    return render(request, 'photography/create_post.html', context)

def explore(request):
    queryset = Post.objects.all()
    context = {'object_list': queryset}
    return render(request, 'photography/explore.html', context)

