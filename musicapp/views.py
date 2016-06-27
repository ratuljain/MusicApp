from django.shortcuts import render
from .forms import AddTrackForm
from django.http import HttpResponse
from .models import Track
from . import getAlbumArt

# Create your views here.
def home(request):
    tracks = Track.objects.all().order_by('created_date')
    return render(request, 'musicapp/post_list.html', {'posts': tracks})

# def post_new(request):
#     form = AddTrackForm()
#     return render(request, 'musicapp/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = AddTrackForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            artist = request.POST.get("artist", "")
            album = request.POST.get("album", "")
            # print artist, album
            urlArt = getAlbumArt.getAlbumArtURL(album, artist)
            print urlArt
            if urlArt:
                post.cover_image_url = urlArt
            post.save()
            tracks = Track.objects.all().order_by('created_date')
            return render(request, 'musicapp/post_list.html', {'posts': tracks})
    else:
        form = AddTrackForm()
    return render(request, 'musicapp/post_edit.html', {'form': form})
