from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *

def insert_topic(request):
    tn=input()
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('TOPIC IS CREATED')
def insert_WebPages(requset):
    tn=input()
    n=input()
    u=input()

    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]
        WO=WebPages.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
        WO.save()
        return HttpResponse('WEBPAGES CREATED')
    else:
        return HttpResponse('NO SUCH TOPIC')

def insert_AccessRecord(requset):
    tn=input()
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
    AO.save()
    return HttpResponse('ACCESSRECORD CREATED')

def display_topic(request):
    QLOT=Topic.objects.all()
    d={'QLOT':QLOT}
    return render(request,'display_topic.html',d)


def display_webpages(request):
    WOTP=WebPages.objects.all()
    d={'WOTP':WOTP}
    return render(request,'display_webpages.html',d)

def display_accessrecord(request):
    ACRD=AccessRecord.objects.all()
    d={'ACRD':ACRD}
    return render(request,'display_accessrecord.html',d)
