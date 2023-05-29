from django import template

register = template.Library()


@register.filter
def format_time(value):
    new = value.strftime("%b %d %H:%M")
    return new
