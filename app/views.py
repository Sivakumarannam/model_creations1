from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

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

def insert_topics(request):
    tn=input('Enter topic: ')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    # return HttpResponse('Topic is created successfully!!!')
    return render(request,'display_topics.html')

def insert_webpage(request):
    tn=input('Enter topic name: ')
    n=input('Enter name: ')
    u=input('Enter url: ')
    e=input('Enter email: ')
    TO=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    NWO.save()
    # return HttpResponse('Webpage is created!!!!!!!!')
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpages.html',d)


def insert_access_records(request):
    pk=input('Enter pk value of webpage: ')
    a=input('Enter author name: ')
    d=input('Enter date : ')
    WO=Webpage.objects.get(name=pk)
    NAO=AccessRecords.objects.get_or_create(name=WO,author=a,date=d)[0]
    NAO.save()
    # return HttpResponse('AcessRecord is created')
    QLARO=AccessRecords.objects.all()
    d={'access':QLARO}
    return render(request,'display_access_records.html',d)

def insert_players(request):
    pk=input('Enter pk value of access_record: ')
    p=input('enter player: ')
    PO=AccessRecords.objects.get(author=pk)
    NPO=Players.objects.get_or_create(author=PO,player=p)[0]
    NPO.save()
    # return HttpResponse('Players is created')
    QLPO=Players.objects.all()
    d={'players':QLPO}
    return render(request,'display_players.html',d)



