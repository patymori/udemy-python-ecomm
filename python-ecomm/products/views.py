from datetime import datetime

from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product


class ProductFeaturedListView(ListView):
    queryset = Product.objects.all().featured()
    template_name = "products/list.html"

    # def get_queryset(self, *args, **kwargs):
    #     return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     return Product.objects.featured()


class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


class ProductDetailView(DetailView):
    # model = Product
    # queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,
                                                                  **kwargs)
        print(context)
        context['now'] = datetime.now()
        return context

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        product = Product.objects.get_by_id(pk)
        if not product:
            raise Http404("Product not found")
        return product

    # def get_queryset(self, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        # product = get_object_or_404(Product, slug=slug, active=True)
        try:
            product = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found")
        except Product.MultipleObjectsReturned:
            queryset = Product.objects.filter(slug=slug, active=True)
            product = queryset.first()
        except:
            raise Http404("* Thinking *")
        return product


def product_detail_view(request, pk=None, *args, **kwargs):
    # product = Product.objects.get(pk=pk)
    # product = get_object_or_404(Product, pk=pk)
    # try:
    #     product = Product.objects.get(pk=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product not found")
    # except:
    #     print('huh?')

    product = Product.objects.get_by_id(pk)
    if product is None:
        raise Http404("Product not found")

    # print(product)
    #
    # qs = Product.objects.filter(pk=pk)
    # if qs.exists() and qs.count() == 1:
    #     product = qs.first()
    # else:
    #     raise Http404("Product not found")

    context = {
        'product': product
    }
    return render(request, "products/detail.html", context)
