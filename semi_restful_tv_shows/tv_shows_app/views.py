from django.shortcuts import render, redirect
from .models import Show
from time import gmtime, strftime
from datetime import datetime, time, timezone


def home(request): 
    context = {
        "shows": Show.objects.all()
    }
    return render(request, "home.html", context)

def add_show(request):
    show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    return redirect(f'/shows/{show.id}')

def TvShow(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'view_shows.html', context)

def AllShows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'all_shows.html', context)

def EditShow(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'edit_shows.html', context)

def UpdateShow(request, id):
    show = Show.objects.get(id=id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.save()
    return redirect(f'/shows/{id}')

def DeleteShow(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')

def index(request):
    return redirect('/shows')
