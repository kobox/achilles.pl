from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from .models import Category, Product, ProductImage
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from fm.views import AjaxCreateView
from .forms import SignUpForm

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


class TestView(AjaxCreateView):
    form_class = SignUpForm


def add_quote(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            #post_save.connect(send_update, sender=Book)
            # Now call the index() view.
            # The user will be shown the homepage.
            return redirect('/thanks/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = SignUpForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('add_signup.html', {'form': form}, context)


class ThanksPage(TemplateView):
    template_name = "thanks.html"