from django.shortcuts import render,get_object_or_404
from .models import About
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def about(request):
    about = About.objects.all()
    return render(request,'about.html',{'about': about })


def detail(request, abouts_id):
    abouts = About.objects.all()
    aboutst = get_object_or_404(About, pk=abouts_id)
    return render(request,'about.html',{'aboutst':aboutst,'about':abouts,})




#return HttpResponseRedirect(reverse('detail'))