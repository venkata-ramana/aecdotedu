from django.shortcuts import render
from django.views.generic.dates import YearArchiveView,MonthArchiveView
# Create your views here.
from .models import NewsPaperArticles
from django.db.models import Count
from datetime import date,time
from django.core.paginator import Paginator
from django.utils import timezone

class ArticleYearArchiveView(YearArchiveView):
    model = NewsPaperArticles
    queryset = NewsPaperArticles.objects.all()
    date_field = "date"
    make_object_list = True
    allow_future = True
    template_name = 'archive_year.html'

class ArticleMonthArchiveView(MonthArchiveView):
    queryset = NewsPaperArticles.objects.all()
    date_field = "date"
    make_object_list = True
    allow_future = True
    model = NewsPaperArticles
    template_name = 'archive_month.html'

def index(request):
    return render(request,'archives.html')
