from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.


class Topic(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=self.model.PUBLISHED)

    def get_authors(self):
        User = get_user_model()
        return User.objects.filter(blog_posts__in=self).distinct()


class Post(models.Model):

    """
    Represents a blog post
    """
    objects = PostQuerySet.as_manager()
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    topics = models.ManyToManyField(
        Topic,
        related_name='blog_posts'
    )
    title = models.CharField(
        max_length=255,
    )
    slug = models.SlugField(
        null=False,
        unique_for_date='published',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='blog_posts',
        null=False,
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible',
    )
    popular = models.BooleanField(
        default=False
    )
    content = models.TextField()
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date and time this article was published',
    )
    created = models.DateTimeField(auto_now_add=True)  # This is set on creation
    updated = models.DateTimeField(auto_now=True)  # This gets updated after each save

    def publish(self):
        self.status = self.PUBLISHED
        self.published = timezone.now()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    comments for each blog post
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    name = models.CharField(
        max_length=100,
    )
    email = models.CharField(
        max_length=100,
    )
    text = models.CharField(
        max_length=500
    )
    approved = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def not_approved(self):
        self.approved = False
        self.save()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.text[:50]
