from django.shortcuts import render
from . import models
from django.db.models import Count
# Create your views here.


def home(request):
    """
    home view
    """
    latest_posts = models.Post.objects.published().order_by('-published')[:3]
    authors = models.Post.objects.published().get_authors().order_by('first_name')
    top_posts = models.Post.objects.filter(comments__approved=True).annotate(total_comments=Count('comments')).order_by('-total_comments')[:10]
    for post in models.Post.objects.all():
        if post in top_posts:
            post.popular = True
            post.save()
        else:
            post.popular = False
            post.save()

    sorted_topics = models.Topic.objects.filter(blog_posts__popular=True).annotate(total_posts=Count('blog_posts')).order_by('-total_posts')
    all_topics = models.Topic.objects.all()

    context = {
        'authors': authors,
        'latest_posts': latest_posts,
        'sorted_topics': sorted_topics,
        'all_topics': all_topics,
    }

    return render(request, 'blog/home.html', context)
