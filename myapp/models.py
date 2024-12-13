from django.db import models

# Create your models here.
class Authors(models.Model):
    full_name=models.CharField(max_length=40,null=False,verbose_name='ФИО пассажира')
    birth_date=models.IntegerField(null=False,verbose_name='Дата рождения')
    country_citizen=models.CharField(max_length=100,null=False,verbose_name='Страна проживания')
class Books(models.Model):
    name=models.CharField(max_length=50,null=False,verbose_name='название книги',unique=True)
    genre=models.CharField(max_length=40,null=False,verbose_name='жанр')
    year=models.IntegerField(null=False,verbose_name='год написания')
    author_id=models.ForeignKey(Authors,verbose_name='id автора',on_delete=models.CASCADE,null=False)