from django import template
from ride.models import Place

register = template.Library()

@register.filter
def to_place(location):
    return Place.objects.get(location=location).name