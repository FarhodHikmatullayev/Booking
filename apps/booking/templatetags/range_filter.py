from django import template

register = template.Library()

@register.filter()
def range_filter(stop, args_str):
    start, step = args_str.split(',')   # "1, 1" -> ['1', '1']
    return range(int(start), stop+1, int(step))
