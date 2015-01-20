from django.shortcuts import render

# Create your views here.
def downloads_all(request):
    return render(request,'downloads.html')