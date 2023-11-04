from django.shortcuts import render, get_object_or_404
from . models import Category, Product
# Create your views here.


def product_list(request, category_slug=None):
    """
    if there is no slug --> no category
    bring all another catgeories and products
    else bring category object and products related to that object 
    """
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)

    return render(
        request,
        'shop/product/list.html',
        {
            'section':category,
            'categories':categories,
            'products':products
        }
    )



def product_detail(request, slug, id):
    """
    return product object 
    """
    product = get_object_or_404(Product, 
                                slug=slug,
                                id=id,
                                available=True)
    return render(
        request,
        'shop/product/detail.html',
        {
        'product': product
        }
    )