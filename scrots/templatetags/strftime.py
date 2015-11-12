from django import template

register = template.Library()


@register.filter(name="format")
def format_date(date, date_format):
    """
    Template tag filter takes a strftime string and returns the formated date
    """
    return date.strftime(date_format)
