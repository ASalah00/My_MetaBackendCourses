from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render
def my404handler(request,exception):
    return HttpResponseNotFound("no page like this idiot")
    # return HttpResponse("paqge mesh mwgoda 404 ahaha",status=404)
    # return render(request, '404.html', status=404)