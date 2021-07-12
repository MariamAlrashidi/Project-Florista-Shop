
from django.shortcuts import render , HttpResponse , redirect
from django.http import JsonResponse
from datetime import datetime
from .models import CartItem, Categories , Cart
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages





# Create your views here.

# path('home/')
def home(request):
    return  render(request,'home.html' , {}) 

# path('Categories/')

def categories(request): 
    all_categories = Categories.objects.all()
    return render(request , 'home.html' , 
    {"all_categories" : all_categories  })
 

def show_categories(request , pk):
    id_=pk
    try:
        one_category = Categories.objects.get(id=pk)
        print(one_category)
    except Exception:
        return HttpResponse("error")
    
    return render(request , 'categories/show.html' ,
    {   
    "one_category" : one_category
    } )


@login_required()
def add_to_cart(request, pk):

    user = User.objects.get(pk = request.user.id) 
    product = Categories.objects.get(id=pk)

    order_item = CartItem.objects.create(product=product)
    cart  = Cart.objects.filter(owner=user, is_ordered=False).count()

    print(cart)
    if cart == 0:
        cart  = Cart.objects.create(owner=user, is_ordered=False)
        cart.items.add(order_item)
        cart.save()
    else:
        cart  = Cart.objects.get(owner=user, is_ordered=False)
        cart.items.add(order_item)
        cart.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect('/categories')


def get_user_order(request):
    # get order for the correct user
    user = User.objects.get(pk = request.user.id) 
    cart = Cart.objects.filter(owner=user, is_ordered=False)
    if cart.exists():
        return cart[0]
    return 0

@login_required()
def cart_details(request):
    cart = get_user_order(request)
    context = {
        'cart': cart
    }

    return render(request, 'cart/cartsum.html', context)


@login_required()
def delete_from_cart(request, pk):
    cart_item = CartItem.objects.filter(pk=pk)
    if cart_item.exists():
        cart_item[0].delete()
        messages.warning(request, "Item has been deleted")
    return redirect('/cart')

def collect_from_store(request):
    return  render(request,'cart/collectstore.html' , {}) 