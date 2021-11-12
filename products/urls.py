from django.urls import path, include, re_path
from products.views import ProductView

urlpatterns = [
    re_path(r'',ProductView.as_view())
]