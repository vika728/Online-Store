from .models import Category, Product, ReviewProduct


def get_categories(request):
    categories = Category.objects.all()
    categories_5 = Category.objects.all()[0:5]
    return {'categories': categories, 'categories_5': categories_5}
