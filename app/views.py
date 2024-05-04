from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length
# Create your views here.
from app.models import *

def insert_topic(request):
    tn=input()
    d={'QLOT':Topic.objects.all()}
    
    
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return render(request,'display_topic.html',d)
    
def insert_WebPages(request):
    tn=input()
    n=input()
    u=input()
    

    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]
        WO=WebPages.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
        WO.save()
        d={'WOTP':WebPages.objects.all()}
        return render(request,'display_webpages.html',d)
    else:
        d={'QLOT':Topic.objects.all()}
        return render(request,'display_topic.html',d)

def insert_AccessRecord(request):
   ''' tn=input()
    TO=Topic.objects.create(topic_name=tn)[0]
    TO.save()
    
    n=input()
    u=input()
    e=input()
    WO=WebPages.objects.create(topic_name=TO,name=n,url=u)[0]
    WO.save()

    d=input()
    a=input()
    AO=AccessRecord.objects.create(name=WO,data=d,author=a)[0]
    AO.save()'''
   n=input()
   WO=WebPages.objects.get(id=n)
   d=input('enter date')
   a=input('enter author')
   AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
   AO.save()
   d={'ACRD':AccessRecord.objects.all()}
   return render(request,'display_accessrecord.html',d)

   return HttpResponse('ACCESSRECORD CREATED')
 
def display_topic(request):
    QLOT=Topic.objects.all()
    d={'QLOT':QLOT}
    return render(request,'display_topic.html',d)


def display_webpages(request):
    WOTP=WebPages.objects.all()
    WOTP=WebPages.objects.filter(topic_name='cricket')
    WOTP=WebPages.objects.exclude(topic_name='cricket')
    WOTP=WebPages.objects.all()[::-1]
    WOTP=WebPages.objects.all().order_by('name')
    WOTP=WebPages.objects.all().order_by('-name')
    WOTP=WebPages.objects.all().order_by(Length('name'))
    WOTP=WebPages.objects.all().order_by(Length('name').desc())
    WOTP=WebPages.objects.filter(name__startswith='j')
    WOTP=WebPages.objects.filter(name__endswith='n')
    WOTP=WebPages.objects.filter(name__contains='J')
    WOTP=WebPages.objects.filter(name__in=('john','praveen'))





    d={'WOTP':WOTP}
    return render(request,'display_webpages.html',d)

def display_accessrecord(request):
    ACRD=AccessRecord.objects.all()
    ACRD=AccessRecord.objects.filter(date__year='2024')
    ACRD=AccessRecord.objects.filter(date__month='12')
    ACRD=AccessRecord.objects.filter(date__day='10')
    ACRD=AccessRecord.objects.filter(date__gt='2024-12-12')
    ACRD=AccessRecord.objects.filter(date__gte='2024-12-12')
    ACRD=AccessRecord.objects.filter(date__lt='2024-12-12')
    ACRD=AccessRecord.objects.filter(date__lte='2024-11-13')
    ACRD=AccessRecord.objects.filter(date__year__gte='2024')
    
    
    
    
    
    

   
    
    d={'ACRD':ACRD}
    return render(request,'display_accessrecord.html',d)





