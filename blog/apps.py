"""
blog app
"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    blog app config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
