from django import template

from authentication.models import Chapter

register = template.Library()


@register.filter
def get_chapter_locations():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@####################")
    locations = []
    for chapter in Chapter.objects.all():
        locations.append(chapter.get_coordinates)
    return locations
