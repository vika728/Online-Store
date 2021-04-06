from .models import Category, Product, ReviewProduct


def get_categories(request):
    categories = Category.objects.all()
    categories_5 = Category.objects.all()[0:5]
    return {'categories': categories, 'categories_5': categories_5}


def get_products(request):
    products = Product.objects.all()[0:6]
    products_4 = Product.objects.all()[0:4]
    category = Category.objects.get(slug='supyi')
    products_category = Product.objects.filter(category=category)
    category_napitki = Category.objects.get(slug='napitki')
    products_napitki = Product.objects.filter(category=category_napitki)

    products_count = Product.objects.all().count()

    context = {
        'products': products,
        'products_4': products_4,
        'products_category': products_category,
        'products_napitki': products_napitki,
        'products_count': products_count
    }
    return context