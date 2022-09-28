from datetime import datetime
from time import strptime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from website.models import Post
from django.utils import timezone
def index_view(request):
    return render(request,'website/index.html')
def HW(request):
    posts = Post.objects.exclude(published_date__gt=datetime.now())
    context = {'posts': posts}
    for post in posts:
        post.counted_view += 1
        post.save()
    return render(request,'website/HW.html',context)