from django.shortcuts import render

# Create your views here.

app_name = "cart"

from goods.models import Product
from cart.models import CartItem

def GetCart():
    TotalSum = 0

    context = {
        "CartItems" : list(),
        "TotalSum": 0,
    }

    for Item in CartItem.objects.all():
        ItemProd = Product.objects.get(id=Item.ItemId)
        TotalPrice = Item.Amount * ItemProd.price
        TotalSum += TotalPrice
        context["CartItems"].append({
            "Id": ItemProd.id,
            "Amount": Item.Amount,
            "Name": ItemProd.name,
            "Price": ItemProd.price,
            "TotalPrice": TotalPrice,
        })
    context["TotalSum"] = TotalSum
    return context

def cart(request):
    if request.method == "POST":
        if request.POST.get("Action") == "Delete":
            Item = CartItem.objects.get(ItemId=request.POST.get("ProdId"))
            Item.delete()
            


    context = GetCart()

    return render(request, "cart/cart.html", context)

def order(request):
    context = GetCart()

    return render(request, "cart/formalization.html", context)
