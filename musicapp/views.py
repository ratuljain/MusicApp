from django.shortcuts import render
from .forms import AddTrackForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'musicapp/post_list.html', {})

def post_new(request):
    form = AddTrackForm()
    return render(request, 'musicapp/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = AddTrackForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return render(request, 'musicapp/post_list.html', {})
    else:
        form = AddTrackForm()
    return render(request, 'musicapp/post_edit.html', {'form': form})
