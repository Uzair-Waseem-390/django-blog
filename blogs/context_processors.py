from .models import Category


def blog_categories(request):
    """
    A context processor that adds all blog categories to the context.
    """
    categories = Category.objects.all()
    return dict(categories=categories)