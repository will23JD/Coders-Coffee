from django.shortcuts import render, get_object_or_404
from .models import Blog

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
