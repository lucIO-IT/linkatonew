from django import template
register = template.Library()

@register.filter(name='followers')
def followers_list(corso):
    followers = corso.followers.all()
    return followers