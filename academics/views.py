from django.shortcuts import render,get_object_or_404
from .models import AcademicsInfo
# Create your views here.
def academics(request):
    academics = AcademicsInfo.objects.all()
    return render(request,'academics.html',{'academics': academics })


def adetail(request, academics_id):
    academics = AcademicsInfo.objects.all()
    adetail = get_object_or_404(AcademicsInfo, pk=academics_id)
    return render(request,'academics.html',{'adetail':adetail,'academics':academics,})