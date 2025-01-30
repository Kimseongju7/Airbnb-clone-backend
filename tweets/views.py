from django.shortcuts import render
from .models import Tweet
from django.http import HttpResponse

# Create your views here.
def all_tweets(request):
    tweets = Tweet.objects.all()
    return HttpResponse("hello world")