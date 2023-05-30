from django.http import HttpResponse

def index(request):
    return HttpResponse('This is the beginning of my blog about Guild Wars 2 (aka GW2).')