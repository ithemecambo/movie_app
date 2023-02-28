from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Movie app review page")


def about(request):
    return HttpResponse("About page")


def signup(request):
    return HttpResponse("Signup page")


def login(request):
    return HttpResponse("Login page")