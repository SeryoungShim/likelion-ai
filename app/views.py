from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Photo

# Create your views here.
@csrf_exempt
def photo(request):
    photos = Photo.objects.all()
    photos_ = []
    for photo in photos:
        photos_.append({"id":photo.id, "url": photo.url})
    return JsonResponse({
        'statusCode': 200,
        'body': {"photos": photos_}
    })
    # return render(request, "photo.html", {"photos": photos_})