from .models import Category
from home.models import FollowUs

def blog_categories(request):
    """
    A context processor that adds all blog categories to the context.
    """
    categories = Category.objects.all()
    return dict(categories=categories)


def follow_us_links(request):
    """
    A context processor that adds follow us links to the context.
    """
    follow_us_info = FollowUs.objects.all()
    return dict(follow_us_info=follow_us_info)