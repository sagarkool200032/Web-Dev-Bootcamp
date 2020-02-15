from django import template

register = template.Library()

def change(value,arg):
    """
    """
    return value.replace(arg,"")

register.filter("change",change)