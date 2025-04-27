from django.urls import path
from goods import views
from goods.views import ProductDetailView, categories
app_name = "goods"

urlpatterns = [
    path('', categories.as_view(), name="categories"),
    path('<pk>/', ProductDetailView.as_view(), name="product")
]
