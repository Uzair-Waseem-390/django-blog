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
    # print(slug)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        # comment = Comment()
        # comment.user = request.user
        # comment.blog = BlogPost.objects.get(slug=slug)
        # comment.comment = request.POST.get('comment')
        # comment.save()
        Comment.objects.create(
            user=request.user,
            blog=BlogPost.objects.get(slug=slug),
            comment=request.POST.get('comment')
        )
        return redirect('blog_detail', slug=slug)
    comment = Comment.objects.filter(blog__slug=slug).order_by('-created_at')
    # print(comment)
    comment_count = comment.count()
    try:
        blog_post = BlogPost.objects.get(slug=slug, status="Publish")
    except BlogPost.DoesNotExist:
        return redirect('home')
    
    
    context = {
        'blog_post': blog_post,
        'comments': comment,
        'comment_count': comment_count
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


# def add_comment(request, slug):
#     if request.method == 'POST':
#         blog_post = get_object_or_404(BlogPost, slug=slug, status="Publish")
#         content = request.POST.get('content')
#         author = request.user

#         Comment.objects.create(
#             blog=blog_post,
#             author=author,
#             content=content
#         )
#     return redirect('blog_detail', slug=slug)
# from django.db import models