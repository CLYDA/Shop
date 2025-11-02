from django.shortcuts import render , get_object_or_404
from .models import Product , Category


def product_list(request, category_slug=None):
    category = None
    categories = category.objects.all()
    products = product.objects.all()
    if category_slug:
        category = get_object_or_404(category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'shop/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'shop/detail.html', product)

  