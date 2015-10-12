from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag(takes_context=True)
def user_is_watching(context, website, btn_class='watch-website-btn'):
    """
    Template tag that returns the HTML for the watching icon for Websites.
    """
    user = context['request'].user
    watching_html = (
        '<a href="" title="{}">'
        '<i class="glyphicon glyphicon-eye-open {} {}"></i>'
        '</a>'
    )
    if user.is_authenticated():
        # If the user is not anonymous, find out if she is watching the Website
        if user.likes_website(website):
            return watching_html.format("Watching", settings.WATCHING_CLASS, btn_class)
        else:
            return watching_html.format("Start Watching", '', btn_class)
    else:
        return ''
