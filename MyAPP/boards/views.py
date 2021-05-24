# from django.shortcuts import render
#
# # Create your views here.

from django.http import httpResponse
def home(request):
    return httpResponse('hello,world!')