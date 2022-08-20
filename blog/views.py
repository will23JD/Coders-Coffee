from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    """ Return blog page """
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog.html', context)
