from django import template

register = template.Library()

@register.filter
def estilo(data):
    return data.strftime('%d/%m/%Y - %H:%Mh')



