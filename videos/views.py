from django.shortcuts import render

# Create your views here.

from .models import Video
def index(request):
    videos = Video.objects.all()
    
    return render(request , 'index.html' , {
        'videos': videos
    })