from model_bakery import baker
import pytest

from blog.models import Post
pytestmark = pytest.mark.django_db


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200


def test_authors_included_in_context_data(client, django_user_model):
    """
    Checks that a list of unique published authors is included in the
    context and is ordered by first name.
    """
    cosmo = baker.make(
        django_user_model,
        username='ckramer',
        first_name='Cosmo',
        last_name='Kramer'
    )
    baker.make(
        'blog.Post',
        status=Post.PUBLISHED,
        author=cosmo,
        _quantity=2
    )
    elaine = baker.make(
        django_user_model,
        username='ebenez',
        first_name='Elaine',
        last_name='Benez'
    )
    baker.make(
        'blog.Post',
        status=Post.PUBLISHED,
        author=elaine,
    )
    unpublished_author = baker.make(
        django_user_model,
        username='gcostanza'
    )
    baker.make('blog.Post', author=unpublished_author, status=Post.DRAFT)

    expected = [cosmo, elaine]

    response = client.get('/')

    result = response.context.get('authors')

    assert list(result) == expected
