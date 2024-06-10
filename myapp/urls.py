from django.urls import path
from .views import index_html, about_html, category_html, work_html

urlpatterns = [
    path('',index_html, name="index_html"),
    path('about_html',about_html, name="about_html"),
    path('category_html',category_html, name="category_html"),
    path('work_html',work_html, name="work_html")
]