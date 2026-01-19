from django.shortcuts import render
from blogs.models import Category, BlogPost as Post
from .forms import CategoryForm, PostForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def dashboard(request):
    categories = Category.objects.all()
    posts = Post.objects.select_related('category').all()
    context = {'categories': categories, 'posts': posts}
    return render(request, 'dashboards/dashboard.html', context)


@login_required(login_url='login')
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'dashboards/edit_category.html', {'form': form})

@login_required(login_url='login')
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('dashboard')

@login_required(login_url='login')
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'dashboards/edit_post.html', {'form': form})

@login_required(login_url='login')
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('dashboard')


@login_required(login_url='login')
def add_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'dashboards/add_category.html', {'form': form})


@login_required(login_url='login')
def add_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('dashboard')
    return render(request, 'dashboards/add_post.html', {'form': form})