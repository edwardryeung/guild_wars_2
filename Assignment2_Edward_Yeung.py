from django.contrib.auth import get_user_model
from django.db.models import Count, Q

from blog.models import Comment, Post

User = get_user_model()


def question_1_return_active_users():
    """
    Return the results of a query which returns a list of all
    active users in the database.
    """
    return User.objects.filter(is_active=True)


def question_2_return_regular_users():
    """
    Return the results of a query which returns a list of users that
    are *not* staff and *not* superusers
    """
    return User.objects.exclude(Q(is_staff=True) & Q(is_superuser=True))


def question_3_return_all_posts_for_user(user):
    """
    Return all the Posts authored by the user provided. Posts should
    be returned in reverse chronological order from when they
    were created.
    """
    user = User.objects.get(username=user)
    return user.blog_posts.all().order_by('-created')
    # The order_by is redundant for my particular code because
    # Post's meta already specifies sorting by created timestamp in
    # reverse chronological order.


def question_4_return_all_posts_ordered_by_title():
    """
    Return all Post objects, ordered by their title.
    """
    return Post.objects.all().order_by('title')


def question_5_return_all_post_comments(post):
    """
    Return all the comments made for the post provided in order
    of last created.
    """
    post = Post.objects.get(title=post)
    return post.comments.all().order_by('-created')
    # Similarly with question 3, the order_by is redundant because
    # Comment's meta already specifies sorting by created timestamp in
    # reverse chronological order.


def question_6_return_the_post_with_the_most_comments():
    """
    Return the Post object containing the most comments in
    the database. Do not concern yourself with approval status;
    return the object which has generated the most activity.
    """
    return Post.objects.annotate(total_comments=Count('comments')).order_by(
        '-total_comments')[0]


def question_7_create_a_comment(post):
    """
    Create and return a comment for the post object provided.
    """
    post = Post.objects.get(title=post)
    comment = Comment.objects.create(
        post=post,
        name='Stranger',
        email='stranger@example.com',
        text='example comment',
    )
    return comment


def question_8_set_approved_to_false(comment):
    """
    Update the comment record provided and set approved=False
    """
    comment = Comment.objects.get(text=comment)
    return comment.not_approved()


def question_9_delete_post_and_all_related_comments(post):
    """
    Delete the post object provided, and all related comments.
    """
    post = Post.objects.get(title=post)
    return post.delete()
    # I have set comments to be deleted whenever their post gets deleted
    # by specifying on_delete=models.CASCADE
