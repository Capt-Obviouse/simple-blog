from django.shortcuts import render
from .models import Posts

# Create your views here.
def index(request):
    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Latest Post',
        'posts': posts
    }

    return render(request, 'posts/index.html', context)
