from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.

def display_topics(request):
    QLTO= Topic.objects.all()
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().order_by('-topic_name')
    QLTO=Topic.objects.all().order_by(Length('topic_name'))
    QLTO=Topic.objects.all().order_by(Length('topic_name').desc())


    d={'topics':QLTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by(Length('name').desc())
    QLWO=Webpage.objects.filter(topic_name='Cricket')[::]
    QLWO=Webpage.objects.all()
    # QLWO=Webpage.objects.exclude(topic_name='Foot Ball')
    QLWO=Webpage.objects.filter(pk=6)
    QLWO=Webpage.objects.filter(pk__gt=6)
    QLWO=Webpage.objects.filter(pk__lt=4)
    QLWO=Webpage.objects.filter(pk__gte=4)
    QLWO=Webpage.objects.filter(pk__lte=5)
    QLWO=Webpage.objects.filter(name__startswith='s')
    QLWO=Webpage.objects.filter(name__endswith='a')
    QLWO=Webpage.objects.filter(name__contains='i')
    QLWO=Webpage.objects.filter(pk__in=(1,3,4))
    QLWO=Webpage.objects.filter(pk__in=[1,4,6])
    QLWO=Webpage.objects.filter(topic_name='Cricket' , name__startswith='S')
    QLWO=Webpage.objects.filter(topic_name='Cricket', url__endswith='com')
    QLWO=Webpage.objects.filter(name__contains='r',url__endswith='in',email__endswith='com')
    QLWO=Webpage.objects.filter(Q(topic_name='Foot Ball') & Q(name__contains='S'))
    QLWO=Webpage.objects.filter(Q(topic_name='Foot Ball') & Q(name__contains='s') &Q(url__endswith='in') & Q(email__endswith='com'))
    QLWO=Webpage.objects.filter(Q(name__contains='s') | Q(url__endswith='in'))
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket') | Q(email__endswith='com'))
    QLWO=Webpage.objects.filter(topic_name__in=('Kabaddi','Chess','Foot Ball'))
    QLWO=Webpage.objects.all()



    d={'webpages':QLWO}
    return render(request,'display_webpages.html',d)


def display_access_records(request):
    QLARO=AccessRecords.objects.all()
    QLARO=AccessRecords.objects.filter(date__day=10)
    QLARO=AccessRecords.objects.filter(date__day__lt=10)
    QLARO=AccessRecords.objects.filter(date__day__gt=5)
    QLARO=AccessRecords.objects.filter(date__year=2023)
    QLARO=AccessRecords.objects.filter(date__year__gt=2001)
    QLARO=AccessRecords.objects.filter(date__year__lt=2023)
    QLARO=AccessRecords.objects.filter(date__month=12)
    QLARO=AccessRecords.objects.filter(date__month__lt=12)
    QLARO=AccessRecords.objects.filter(date__month__gt=5)
    QLARO=AccessRecords.objects.filter(author__regex='s')


    QLARO=AccessRecords.objects.filter(author__startswith='v',date__month=12)
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


def update_webpage(request):
    Webpage.objects.filter(topic_name='Cricket').update(name='Rakesh')
    Webpage.objects.filter(topic_name='Foot Ball').update(name='Siva')
    Webpage.objects.filter(name='Siva').update(url='https://siva.in',email='siv@gmail.com')
    Webpage.objects.filter(name='deepu').update(url='https://deepu.in',email='deepu@gmail.com')
    Webpage.objects.update_or_create(topic_name='Kabaddi',defaults={'name':'Pawan Sharavat'})
    Webpage.objects.update_or_create(topic_name='Kabaddi',defaults={'name':'Rajesh'})
    UPO=Topic.objects.get_or_create(topic_name='Basket Ball')[0]
    UPO.save()
    Webpage.objects.update_or_create(name='deepu',defaults={'topic_name':UPO})
    Webpage.objects.update_or_create(name='NTR',defaults={'topic_name':UPO,'url':'https://NTR.in','email':'ntr@gmail.com'})
    # Webpage.objects.update_or_create(topic_name='Basket Ball',defaults={'name':'Sai'})
    Webpage.objects.filter(topic_name='Chess').update(name='Venkat')
    Webpage.objects.filter(topic_name='Chess').update(url='https://chess.in',email='chess@gmail.com')
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}

    return render(request,'display_webpages.html',d)

def update_access_records(request):
    AccessRecords.objects.filter(name=4).update(date='1999-07-7')
    AccessRecords.objects.filter(name=6).update(date='2002-12-20')
    AccessRecords.objects.filter(name=7).update(date='2001-12-1')
    AccessRecords.objects.filter(name=1).update(author='rakesh')
    AccessRecords.objects.filter(name=2).update(author='siva')
    AccessRecords.objects.filter(name=4).update(author='sai')
    AccessRecords.objects.filter(name=6).update(author='rajesh')
    AccessRecords.objects.filter(name=7).update(author='venkat')


    QLARO=AccessRecords.objects.all()
    d={'access':QLARO}
    return render(request,'display_access_records.html',d)



