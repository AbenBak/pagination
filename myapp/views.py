from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .data_gen import gen_book,get_author
from django.core.paginator import Paginator,Page
from .models import Books,Authors
# Create your views here.
def view_books(req:HttpRequest)->HttpResponse :
    books=Books.objects.all()
    paging=Paginator(object_list=books,per_page=10,orphans=0,allow_empty_first_page=True,)
    num_page=1
    page=paging.page(num_page)
    if 'page' in req.GET:
        num_page=req.GET['page']
    page=paging.page(num_page)
    return render(req,'books.html',{'page':page,'title': f'Список книг -{num_page}'})
def view_authors(req:HttpRequest)->HttpResponse :
    return render(req,template_name='author.html')
def view_gen_data(req:HttpRequest)->HttpResponse:
    for i in range(10):
        get_author()
    for i in range(20):
        gen_book()
    return HttpResponse('Сгенерированны данные для авторов и книг')