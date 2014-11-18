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
    template_name = 'archive.html'

def newspaperarticles_index(request):
    year_list = NewsPaperArticles.objects.extra(select={'year':"strftime('%%Y',date)"}).values('year').order_by().annotate(Count('id'))
    month_list = NewsPaperArticles.objects.filter.extra(select={'month':"strftime('%%M',date)"}).values('month').order_by().annotate(Count('id'))
    return render(request,'archive_index.html',{'year_list':year_list,})


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = NewsPaperArticles.objects.all()
    date_field = "date"
    make_object_list = True
    allow_future = True
    model = NewsPaperArticles
    template_name = 'archive_month.html'

def mkmonth_lst():
    """Make a list of months to show archive links."""
    if not NewsPaperArticles.objects.count(): return []

# set up vars
    year, month = time.localtime()[:2]
    first = Post.objects.order_by("created")[0]
    fyear = first.created.year
    fmonth = first.created.month
    months = []

# loop over years and months
    for y in range(year, fyear-1, -1):
        start, end = 12, 0
        if y == year: start = month
        if y == fyear: end = fmonth-1
    
        for m in range(start, end, -1):
            months.append((y, m, month_name[m]))
    return months

def archive_index(request):
    """Main listing."""
    posts = NewsPaperArticles.objects.all().order_by("-created")
    paginator = Paginator(posts, 10)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render("archive_index.html", dict(posts=posts, user=request.user,
                                            post_list=posts.object_list,    months=mkmonth_lst()))
