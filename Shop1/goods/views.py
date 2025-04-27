from django.shortcuts import render
from django.views.generic import DetailView, ListView
 
from goods.models import Product
from cart.models import CartItem

# Create your views here.

class categories(ListView):
    model = Product
    template_name = 'goods/category.html'
    context_object_name = 'Products'

    def get_queryset(self):
       result = super(categories, self).get_queryset()
       query = self.request.GET.get('q')
       if query:
          postresult = Product.objects.filter(name__contains=query.capitalize())
          result = postresult
       else:
           result = Product.objects.all()
       return result

# def categories(request):
#     products = Product.objects.all()
#     # query = request.get_queryset()
#     # if query:
#     #     products = query
    
#     context = {
#         "Products" : products,
#     }
#     return render(request, "goods/category.html", context)


class ProductDetailView(DetailView):
    template_name = "goods/product.html"
    model = Product

   

    def get_object(self, queryset = None):
        product = Product.objects.get(id=self.kwargs.get(self.pk_url_kwarg))
        return product

    def get(self, request, *args, **kwargs):
        if request.GET.get("Action") == "Add":
            id = request.GET.get("ProdId")
            Amount = request.GET.get("Quantity")
            try:
                Item = CartItem.objects.get(ItemId=id)
                Item.Amount += int(Amount)
                Item.save()
            except:
                CartItem.objects.create(ItemId = id, Amount=Amount)


        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    


# def product(request):
#     return render(request, "goods/product.html")