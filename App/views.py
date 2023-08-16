from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from . models import Product
from . forms import ProductForm
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.db.models import Q


# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_admin:
            login(request, user)
            return redirect('admin_profile')
        
        else:
            response = HttpResponse('Access barred!')
            return response

    return render(request, 'admin_login.html')

def admin_profile(request):
    #The logic to manage products
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            #redirect showing success message for example

        else:
            product_form = ProductForm()

        products = Product.objects.all() # Retrieving products from the database 
        return render(request, 'admin_profile.html', {'product_form': product_form, 'products':products})
    
# Deleting products listed
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product.delete()
        # Redirect to a page, or show a success message

    return render(request, 'delete_product.html', {'product': product})

# Displaying products on the landing page
def landing_page(request):
    products = Product.objects.all()
    return render(request, 'landing_page.html', {'products': products})

# More details about product(s)
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product_detail.html', {'product': product})


# Searching and displaying products
def search_products(request):
    query = request.GET.get('q')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    selected_brands = request.GET.getlist('brands')

    products = None

    if query or min_price or max_price or selected_brands:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query) |
            Q(color__icontains=query),
            price__gte=min_price, # gte - greater than or equal to
            price__lte=max_price, # lte - less than or equal to
            brand__in=selected_brands
        )

    if selected_brands:
        products = products.filter(selected_brands__icontains=selected_brands)

    return render(request, 'search_results.html', {
        'query': query,
        'products': products,
        'min_price': min_price,
        'max_price': max_price,
        'selected_brands': selected_brands,
        })





class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

