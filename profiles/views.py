from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Wishlist
from .forms import UserProfileForm

from checkout.models import Order
from products.models import Product


@login_required
def wishlist(request):
    """Display user's wishlist"""

    wishitems = Wishlist.objects.filter(user=request.user)
    context = {
        'wishitems': wishitems,
        'on_profile_page': True
    }

    return render(request, 'profiles/wishlist.html', context)


@login_required
def add_to_wishlist(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    if request.method == 'POST':
        wish_item = Wishlist.objects.filter(user=request.user, product=product)
        if wish_item:
            messages.info(request, 'Product already in Wishlist')
        else:
            messages.success(request, 'Added to Wishlist')
            Wishlist.objects.create(user=request.user, product=product, size=size)


    return redirect(redirect_url)


@login_required
def delete_from_wishlist(request, item_id):
    """ Delete a product from the wishlist """

    product = get_object_or_404(Product, pk=item_id)
    Wishlist.objects.filter(product=product).delete()
    messages.success(request, 'Product Removed!')
    return redirect(reverse('wishlist'))



@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Delivery information updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'orders': orders,
        'form': form,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, template, context)


def leave_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # messages.info(request, (
    #     f'This is a past confirmation for order number {order_number}. '
    #     'A confirmation email was sent on the order date.'
    # ))

    template = 'products/product_detail.html'
    context = {
        'product': product,
        'from_profile': True
    }

    return render(request, template, context)
