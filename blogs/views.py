from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect


from blogs.models import *

# Create your views here.
def post_by_category(request, category_id):
    posts = BlogPost.objects.filter(category__id=category_id, status="Publish").order_by('-created_at')
    # try:
    #     category = Category.objects.get(id=category_id)
    # except Category.DoesNotExist:
    #     return redirect('home')
    category = get_object_or_404(Category, id=category_id)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)