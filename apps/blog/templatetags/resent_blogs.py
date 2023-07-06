from django import template
from ..models import Blog, Tag

register = template.Library()


@register.simple_tag()
def resent_blog():
    return Blog.objects.order_by('-id')[:3]


@register.simple_tag()
def get_tags():
    return Tag.objects.all()
