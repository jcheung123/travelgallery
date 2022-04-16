from django.shortcuts import render, redirect
import os
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'travelgallerybucket'


# Create your views here.


def default_map(request):
    my_map_token = os.environ['mapbox_access_token']
    return render(request, 'default.html', {'my_map_token': my_map_token})


def aboutMapBox(request):
    return render(request, 'aboutMapBox.html')


def maps_index(request):
    return render(request, 'maps/index.html')


