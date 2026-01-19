from django import forms
from blogs.models import Category, BlogPost

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
        widgets = {
            'category_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name'
            }),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title', 'slug', 'category', 'featured_image',
            'short_description', 'content', 'status', 'is_featured'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter slug (optional)'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Short description'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post content', 'rows': 5}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input ml-2'}),
        }
