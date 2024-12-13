from .models import Authors,Books
from random import choice,randint
list_authors=[
    'Пушкин А.С.','Лермонтов М.Ю.','Шекспир У.','Абай К.','Достоевский Ф.М.','Шекли','Лем С'
]
list_countries=['Россия','Казахстан','Америка','Франция']
def rand_str(min_length,max_length):
    length=randint(min_length,max_length)
    str_res=chr(randint(ord('A'),ord('Z')))
    for i in range(length-1):
        str_res+=chr(randint(ord('a'),ord('z')))
    return str_res
def get_author():
    # a=Authors()
    # a.full_name=choice(list_authors)
    # a.birth_date=randint(1000,2024)
    # a.country_citizen=choice(list_countries)
    # a.save()
    a=Authors(full_name=choice(list_authors),
              birth_date=randint(1000,1990),
              country_citizen=choice(list_countries))
    a.save()
list_genre=['Роман','Повесть','Фантастика','Поэзия','Научная-Фантастика','Детектив','Очерк']
def gen_book():
    authors_all_id=list(Authors.objects.all().values_list('id'))
    sel_author_id=choice(authors_all_id)[0]
    sel_auth=Authors.objects.get(pk=sel_author_id)
    sel_auth.birth_date
    b=Books()
    b.name=rand_str(5,12) + ' ' + rand_str(7,20)
    b.year=sel_auth.birth_date+randint(13,60)
    b.genre=choice(list_genre)
    b.author_id=sel_auth
    #b.author_id
    b.save()