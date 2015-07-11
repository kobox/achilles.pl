from django.views.generic import DetailView, ListView
from django.views.generic.detail import SingleObjectMixin
from .models import Category, Product, ProductImage


class CategoryDetail(SingleObjectMixin, ListView):
    paginate_by = 2
    template_name = "category_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
        return super(CategoryDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['category'] = self.object
        context['product_list'] = Product.objects.filter(category=self.object)
        return context


class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    model = Product
    #context_object_name = 'product'
    #def get(self, request, *args, **kwargs):
    #    self.object = self.get_object(queryset=Product.objects.all())
    #    return super(ProductDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product_images'] = ProductImage.objects.filter(product=self.get_object())
        return context