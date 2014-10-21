from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from news_events.models import News
from news_events.models import Event
from news_events.models import Carosel
# Create your views here.
def index(request):
	return render(request,'index.html',{'news':News.objects.order_by('-date_time')[:7],'event':Event.objects.order_by('-date_time_updated')[:7],'images':Carosel.objects.all()})
	