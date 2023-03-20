import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WAD_group_project.settings')

import django
django.setup()
from rango.models import Movie, Page

def populate():
    
    python_pages = [
    {'title': 'Official Python Tutorial',
    'url':'http://docs.python.org/3/tutorial/'},
    {'title':'How to Think like a Computer Scientist',
    'url':'http://www.greenteapress.com/thinkpython/'},
    {'title':'Learn Python in 10 Minutes',
    'url':'http://www.korokithakis.net/tutorials/python/'} ]

    django_pages = [
    {'title':'Official Django Tutorial',
    'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
    {'title':'Django Rocks',
    'url':'http://www.djangorocks.com/'},
    {'title':'How to Tango with Django',
    'url':'http://www.tangowithdjango.com/'} ]
    
    other_pages = [
    {'title':'Bottle',
    'url':'http://bottlepy.org/docs/dev/'},
    {'title':'Flask',
    'url':'http://flask.pocoo.org'} ]
    
    movies = {'Harry Potter': {'pages': python_pages},'Cars': {'pages': django_pages}, 'Home Alone': {'pages': other_pages} }
    
    for movie, movie_data in movies.items():
        if (movie=='Harry Potter'):
            c = add_movie(movie, '1982-01-20')
        elif (movie=='Cars'):
            c = add_movie(movie, '1972-02-30')
        elif (movie=='Home Alone'):
            c = add_movie(movie, '1986-03-10')
        for p in movie_data['pages']:
            add_page(c, p['title'], p['url'], random.randint(1,500))
          
    for c in Movie.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')
            
def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p
    
def add_movie(title, releaseDate):
    c = Movie.objects.get_or_create(title=title)[0]
    c.releaseDate=releaseDate
    c.save()
    return c
    
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()