from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag(takes_context=True)
def user_is_watching(context, website):
    """
    Template tag that returns the HTML for the watching icon for Websites.
    """
    user = context['request'].user
    watching_html = (
        '<a href="" title="{}">'
        '<i class="glyphicon glyphicon-eye-open {}">'
        '</i>'
    )
    if user.is_authenticated():
        # If the user is not anonymous, find out if she is watching the Website
        if user.likes_website(website):
            return watching_html.format("Watching", settings.WATCHING_CLASS)
        else:
            return watching_html.format("Start Watching", '')
    else:
        return ''
