from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News
from .models import Event
from .models import Carosel
# Create your views here.
def index(request):
	return render(request,'index.html',{'news':News.objects.order_by('-date_time')[:7],'event':Event.objects.order_by('-date_time_updated')[:7],'images':Carosel.objects.all()})

def allnews(request):
    news_objs = News.objects.all()
    return render(request,'allnews.html',{'news_objs':news_objs})

def allevents(request):
    events_objs = Event.objects.all()
    return render(request,'allevents.html',{'event_objs':events_objs})