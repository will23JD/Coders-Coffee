from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ Return bag page """

    return render(request, 'bag/bag.html')