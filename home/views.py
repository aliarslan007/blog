from django.shortcuts import render
from .models import BlogModel
from django.http import HttpResponse


def home(request):
    blogArticle = BlogModel.objects.all()
    return render(request, 'index.html',
                  {'blogArticle': blogArticle})


def blogpost(request):
    blogArticle = BlogModel.objects.all
    return render(request, 'blogpost.html',
                  {'blogArticle': blogArticle})
