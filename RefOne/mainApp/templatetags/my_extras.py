# Create Own Template Filter

from django import template

register = template.Library()


@register.filter(name='cut')
def cutout(value, arg):
    """
    This cuts out all the values of 'arg' from the string!
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg, '')

# register.filter('cut', cutout)