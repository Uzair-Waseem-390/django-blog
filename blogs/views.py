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


def blog_detail_view(request, slug):
    # blog_post = get_object_or_404(BlogPost, slug=slug, status="Publish")
    print(slug)
    try:
        blog_post = BlogPost.objects.get(slug=slug, status="Publish")
    except BlogPost.DoesNotExist:
        return redirect('home')
    context = {
        'blog_post': blog_post
    }
    return render(request, 'blog_detail.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    results = BlogPost.objects.filter(
        models.Q(title__icontains=keyword) |
        models.Q(short_description__icontains=keyword) |
        models.Q(content__icontains=keyword) |
        models.Q(category__category_name__icontains=keyword) |
        models.Q(author__username__icontains=keyword),
        status="Publish"
    ).order_by('-created_at')
    print(results)
    context = {
        'results': results,
        'keyword': keyword
    }
    return render(request, 'search_results.html', context)