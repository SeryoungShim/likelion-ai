from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Photo

# Create your views here.
@csrf_exempt
def photo(request):
    photos = Photo.objects.all()
    photos_ = []
    for photo in photos:
        photos_.append({"id":photo.id, "url": photo.url})
    return photos_
    # return render(request, "photo.html", {"photos": photos_})