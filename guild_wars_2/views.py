"""
index view
"""

from django.http import HttpResponse

def index(request):
    """
    initial index view to make sure django project works
    """
    return HttpResponse('This is the beginning of my blog about Guild Wars 2 (aka GW2).')
