from django.shortcuts import render_to_response

__author__ = 'ubuntu'


def home(request):
    return render_to_response('home.html')