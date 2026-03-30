from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category

def index(request):
    categories = Category.objects.all()
    query = request.GET.get('q', '').strip()

    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query) |
            Q(manufacturer__name__icontains=query)
        ).distinct()
    else:
        products = products[:6]

    data = {
        'categories': categories,
        'products': products,
        'query': query,
    }
    return render(request, 'home.html', data)


def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    categories = Category.objects.all()
    data = {
        'product': product,
        'categories': categories,
        'query': request.GET.get('q', '').strip(),
    }
    return render(request, 'product.html', data)


def category_products(request, id):
    category = get_object_or_404(Category, pk=id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    data = {
        'category': category,
        'products': products,
        'categories': categories,
        'query': request.GET.get('q', '').strip(),
    }
    return render(request, 'category_products.html', data)

def add_to_cart(request, id):
    cart = request.session.get('cart', {})

    id = str(id)
    if id in cart:
        cart[id] += 1
    else:
        cart[id] = 1

    request.session['cart'] = cart
    return redirect('cart')


def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0
    categories = Category.objects.all()

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        item_total = product.price * quantity
        total += item_total

        products.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total,
        })

    data = {
        'cart_items': products,
        'total': total,
        'categories': categories,
    }
    return render(request, 'cart.html', data)


def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    id = str(id)

    if id in cart:
        del cart[id]

    request.session['cart'] = cart
    return redirect('cart')

def bestsellers(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_bestseller=True)

    data = {
        'categories': categories,
        'products': products,
        'title': 'Bestsellers',
    }
    return render(request, 'category_products.html', data)