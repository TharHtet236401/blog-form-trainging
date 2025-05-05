from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BlogPost
from .forms import BlogPostForm

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog post created successfully!")
            return redirect('blog_list')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_form.html', {'form': form})
