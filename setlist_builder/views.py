from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.conf import settings
from .models import Song
from .serializers import SongSerializer
# from builder import builder
from django.core import serializers
import json


def index(request):
    # number_sets = range(0, 6)
    songs = Song.objects.filter(active=1).order_by('title')
    serializer = SongSerializer(songs, many=True)

    return HttpResponse(
        json.dumps({
            'songs': serializer.data,
        }),
        content_type="application/json"
    )

    # return render(request, 'builder/index.html', {
    #     'songs': songs,
    #     'number_sets': number_sets,
    #     'local_css_urls': settings.CSS_LIBRARY_URLS,
    #     'local_js_urls': settings.JS_LIBRARY_URLS
    # })


def test(request):
    return HttpResponse(
        json.dumps({"message": "It Works!!!"}),
        content_type="application/json"
    )
