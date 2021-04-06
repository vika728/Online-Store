from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

from apps.product.forms import CreateProductForm, CreateReviewProductForm
from apps.product.models import Product, Category, ReviewProduct
from apps.product.permissions import SuperUserCheckMixin


class IndexPage(ListView):
    model = Product
    template_name = 'product/index.html'

    def get_template_names(self):
        template_name = super(IndexPage, self).get_template_names()
        search = self.request.GET.get('search')
        if search:
            template_name = 'product/search.html'
        return template_name

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search')
        if search:
            context['products'] = Product.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'product/category_detail.html'
    context_object_name = 'category'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_products'] = Product.objects.filter(category=self.slug)
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'product/products_list.html'
    context_object_name = 'products'
    paginate_by = 4


class ProductDetailView(View):

    def get(self, request, pk):
        form = CreateReviewProductForm
        product = get_object_or_404(Product, pk=pk)
        reviews = ReviewProduct.objects.filter(product_id=product)
        reviews_count = len(list(reviews))
        return render(request, 'product/product_detail.html', locals())

    def post(self, request, pk):
        user = request.user
        product = get_object_or_404(Product, pk=pk)
        if not user.is_authenticated:
            return redirect(reverse_lazy('login'))
        form = CreateReviewProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(product.get_absolute_url())


class ProductCreateView(SuperUserCheckMixin, CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'product/product_create.html'
    success_url = reverse_lazy('product-create')


class ProductEditView(SuperUserCheckMixin, View):

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = CreateProductForm(instance=product)
        context = {
            'product': product,
            'form': form
        }
        return render(request, 'product/product_update.html', context)

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = CreateProductForm(instance=product, data=request.POST)
        if form.is_valid():
            product = form.save()
            return redirect(product.get_absolute_url())


class ProductDeleteView(SuperUserCheckMixin, DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('products-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.add_message(request, messages.SUCCESS, 'Продукт успешно удален!')
        return HttpResponseRedirect(success_url)


class ReviewIndexPage(ListView):
    model = ReviewProduct
    template_name = 'review_page.html'
    context_object_name = 'all_reviews'