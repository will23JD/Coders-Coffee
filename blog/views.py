from django.shortcuts import render

# Create your views here.
def blog(request):
    """ Return blog page """

    return render(request, 'blog/blog.html')
