from django.shortcuts import render
from blogs.models import Category, BlogPost as Post
from .forms import CategoryForm, PostForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .utils import generate_unique_slug
from django.http import HttpResponseForbidden
from accounts.utils import is_manager, is_editor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from accounts.decorators import manager_required, editor_required, manager_or_editor_required


@login_required(login_url='login')
def dashboard(request):
    if is_editor(request.user):
        categories = Category.objects.all()
        posts = Post.objects.select_related('category').all()
        context = {'categories': categories, 'posts': posts}
        return render(request, 'dashboards/dashboard.html', context)
    elif is_manager(request.user):
        users = User.objects.exclude(id=request.user.id).filter(
        is_superuser=False
        )
    
        context = {
            'users': users,
            'active_page': 'manager_dashboard'
        }

        return render(request, 'dashboards/manager_dashboard.html', context)
    else:
        return HttpResponseForbidden("Bus both ho gaya bacha ghar jao")


@login_required(login_url='login')
@editor_required
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'dashboards/edit_category.html', {'form': form})

@login_required(login_url='login')
@editor_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('dashboard')

@login_required(login_url='login')
@editor_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'dashboards/edit_post.html', {'form': form})

@login_required(login_url='login')
@editor_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('dashboard')


@login_required(login_url='login')
@manager_or_editor_required
def add_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'dashboards/add_category.html', {'form': form})


@login_required(login_url='login')
@manager_or_editor_required
def add_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        if post.slug:
            post.slug = generate_unique_slug(Post, post.slug)   # as BlogPost model is imported as Post
        else:
            post.slug = generate_unique_slug(Post, post.title)
        post.save()
        return redirect('dashboard')
    return render(request, 'dashboards/add_post.html', {'form': form})



@login_required(login_url='login')
@manager_required
def manager_dashboard(request):

    if not is_manager(request.user):
        return HttpResponseForbidden("You are not allowed here")

    users = User.objects.exclude(id=request.user.id).filter(
        is_superuser=False
    )
    
    context = {
        'users': users,
        'active_page': 'manager_dashboard'
    }

    return render(request, 'dashboards/manager_dashboard.html', context)



@login_required(login_url='login')
@manager_required
def edit_user(request, user_id):

    if not is_manager(request.user):
        return HttpResponseForbidden()

    user = get_object_or_404(User, id=user_id)

    if user == request.user:
        return HttpResponseForbidden("You cannot edit yourself")

    form = UserChangeForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('manager_dashboard')

    return render(request, 'dashboards/edit_user.html', {'form': form})


@login_required(login_url='login')
@manager_required
def delete_user(request, user_id):

    if not is_manager(request.user):
        return HttpResponseForbidden()

    user = get_object_or_404(User, id=user_id)

    if user == request.user:
        return HttpResponseForbidden("You cannot delete yourself")

    user.delete()
    return redirect('manager_dashboard')






