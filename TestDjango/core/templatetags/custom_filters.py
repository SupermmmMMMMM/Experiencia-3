from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """
    Función de filtro que multiplica el valor por el argumento dado.
    Ejemplo de uso en una plantilla: {{ value|multiply:arg }}
    """
    try:
        return value * arg
    except (ValueError, TypeError):
        return ''
