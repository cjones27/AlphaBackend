# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the USERS index.")

def create(request):
    return HttpResponse("Aqui se deberia crear un usuario")