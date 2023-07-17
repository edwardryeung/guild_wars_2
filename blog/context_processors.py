from . import models
from django.db.models import Count


def base_context(request):
    authors = models.Post.objects.published().get_authors().order_by('first_name')

    top_posts = models.Post.objects.published().filter(comments__approved=True).annotate(
        total_comments=Count('comments')).order_by('-total_comments')[:10]

    for post in models.Post.objects.published():
        if post in top_posts:
            post.popular = True
            post.save()
        else:
            post.popular = False
            post.save()

    sorted_topics = models.Topic.objects.filter(blog_posts__popular=True).annotate(
        total_posts=Count('blog_posts')).order_by('-total_posts')

    all_topics = models.Topic.objects.all()


    return {
        'authors': authors,
        'sorted_topics': sorted_topics,
        'all_topics': all_topics,
    }
