from django.contrib import admin
from .views import view_authors,view_books,view_gen_data
from django.urls import path,include
urlpatterns = [
    path('books/',view_books,name='view_book'),
    path('authors/',view_authors,name='view_author'),
    path('gen/',view_gen_data,name='view_gen_data')
]