from django.shortcuts import render
from .models import Product

def product_list(request):
    category = request.GET.get('category')  # read ?category=makeup

    if category:
        products = Product.objects.filter(category=category).order_by("-created_at")
    else:
        products = Product.objects.all().order_by("-created_at")

    categories = [
        ('makeup', 'Makeup'),
        ('skincare', 'Skincare'),
        ('fragrance', 'Fragrance'),
        ('haircare', 'Haircare'),
        ('sunscreen', 'Sunscreen'),
        ('other', 'Other'),
    ]

    return render(request, "products/product_list.html", {
        "products": products,
        "categories": categories,
        "selected_category": category
    })
