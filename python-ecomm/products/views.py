from datetime import datetime

from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


class ProductDetailView(DetailView):
    # model = Product
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,
                                                                  **kwargs)
        print(context)
        context['now'] = datetime.now()
        return context


def product_detail_view(request, pk=None, *args, **kwargs):
    # product = Product.objects.get(pk=pk)
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, "products/detail.html", context)
