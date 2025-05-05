from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BlogPost
from .forms import BlogPostForm

def blog_list(request):
    try:
        posts = BlogPost.objects.all().order_by('-created_at')
        return render(request, 'blog/blog_list.html', {'posts': posts})
    except Exception as e:
        messages.error(request, f"An error occurred while fetching blog posts: {str(e)}")
        return render(request, 'blog/blog_list.html', {'posts': []})

def blog_create(request):
    try:
        if request.method == 'POST':
            form = BlogPostForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Blog post created successfully!")
                return redirect('blog_list')
            else:
                messages.error(request, "Error while creating blog post")
        else:
            form = BlogPostForm()
        return render(request, 'blog/blog_form.html', {'form': form})
    except Exception as e:
        messages.error(request, f"An error occurred while creating the blog post: {str(e)}")
        return render(request, 'blog/blog_form.html', {'form': form})
