from django.shortcuts import render
from blogs.models import *
from . models import AboutUs, FollowUs

def home_view(request):
    # categories = Category.objects.all()
    featured_blogs = BlogPost.objects.filter(is_featured=True, status="Publish").order_by('-created_at')[:5]
    posts = BlogPost.objects.filter(is_featured=False, status="Publish").order_by('-created_at')[:5]
    about_us_info = AboutUs.objects.first()
    # follow_us_info = FollowUs.objects.all()
    
    context = {
        # 'categories': categories,         # i comment this because this is coming from context processor now
        'featured_blogs': featured_blogs,
        'posts': posts,
        'about_us_info': about_us_info,
        # 'follow_us_info': follow_us_info  # i comment this because this is coming from context processor now
    }
    return render(request, 'home-blogs.html', context)

