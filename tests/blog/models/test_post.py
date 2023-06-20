from model_bakery import baker
import pytest
from blog.models import Post
import datetime as dt
from freezegun import freeze_time

pytestmark = pytest.mark.django_db


def test_published_posts_only_returns_those_with_published_status():
    published = baker.make('blog.Post', status=Post.PUBLISHED)
    baker.make('blog.Post', status=Post.DRAFT)
    expected = [published]
    result = list(Post.objects.published())
    assert result == expected


def test_publish_sets_status_to_published():
    post = baker.make('blog.Post', status=Post.DRAFT)
    post.publish()
    assert post.status == Post.PUBLISHED


@freeze_time(dt.datetime(2030, 6, 1, 12), tz_offset=0)
def test_publish_sets_published_to_current_datetime():
    post = baker.make('blog.Post', published=None)
    post.publish()
    assert post.published == dt.datetime(2030, 6, 1, 12, tzinfo=dt.timezone.utc)
