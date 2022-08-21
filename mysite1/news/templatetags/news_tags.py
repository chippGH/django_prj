from django import template
from django.db.models import *

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html', name='show_list_categories')
def show_categories(category = None):
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('news', F('news__is_published'))).filter(cnt__gt=0)
    print(categories)
    return {'categories': categories, 'category': category}
