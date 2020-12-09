from django import template

register = template.Library()

@register.filter('Dict_finder')
def Dict_finder(Dict, key):
    if key:
        return Dict.get(key)
