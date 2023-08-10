from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/profile/', views.admin_profile, name='admin_profile'),
    path('search/', views.search_products, name='search_products'),
    path('admin/delete/<int:product_id>/', views.delete_product, name='delete_product'),
]

