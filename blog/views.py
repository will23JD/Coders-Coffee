from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Blog
from .forms import BlogForm

# Create your views here.
def blog(request):
    """ Return blog page """
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    """ Return individual blog details """

    blog_detail = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog_detail': blog_detail,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_blog(request):
    """ Add a blog to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only an admin can access this page.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added blog!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to add blog. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """ Edit a blog in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only an admin can access this page.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Blog!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to update Blog. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)
