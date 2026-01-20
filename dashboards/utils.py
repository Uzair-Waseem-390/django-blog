from django.utils.text import slugify
# import uuid

def generate_unique_slug(model, slug_field_value):
    slug = slugify(slug_field_value)
    unique_slug = slug
    num = 1

    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{slug}-{num}"
        num += 1

    return unique_slug
