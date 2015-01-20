from django.shortcuts import render, get_object_or_404
from .models import InfrastructureInfo
# Create your views here.
def infrastructure(request):
    infrastructure = InfrastructureInfo.objects.all()
    return render(request,'infrastructure.html',{'infrastructure': infrastructure,})
def idetail(request, infrastructure_id):
    infrastructure = InfrastructureInfo.objects.all()
    idetail = get_object_or_404(InfrastructureInfo, pk=infrastructure_id)
    return render(request,'infrastructure.html',{'idetail':idetail,'infrastructure':infrastructure,})