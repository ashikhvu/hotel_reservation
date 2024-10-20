from unittest import result
from django import template

register = template.Library()

@register.filter(name='trimming')
def trimming(val,arg):
    if len(val)>75:
        result1 = val[0:arg]+'......more'
    else:
        result1 = val[0:arg]
    return result1

@register.filter(name='mul')
def mul(val,arg):
    print(val*arg)
    return val*arg