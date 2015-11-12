from django import template

register = template.Library()


@register.filter(name="format")
def format_date(date, date_format):
    """
    Template tag that returns the HTML for the watching icon for Websites.
    """
    return date.strftime(date_format)
