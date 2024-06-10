from django.shortcuts import render
from django.http import HttpResponse

def index_html(request):
    return render(request=request,template_name="index.html")

def about_html(request):
    return render(request=request,template_name="about.html")

def category_html(request):
    return render(request=request,template_name="category.html")

def work_html(request):
    return render(request=request,template_name="work.html")