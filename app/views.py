from django.shortcuts import render
from app.models import *

# Create your views here.

def display_topics(request):
    QLTO= Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpages.html',d)

def display_access_records(request):
    QLARO=AccessRecords.objects.all()
    d={'access':QLARO}
    return render(request,'display_access_records.html',d)

def display_players(request):
    QLPO=Players.objects.all()
    d={'players':QLPO}
    return render(request,'display_players.html',d)
