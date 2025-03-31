from django.shortcuts import render, redirect, HttpResponse
from .models import Product, Category
from .forms import ProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def products_view(request, category_id=None):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)


    return render(request, 'products/products.html', {'page_obj': page_obj, 'categories': categories})


def add_product(request):
    if request.user.is_authenticated and request.user.has_perm('products.add_product'):

        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('products')
            else:
                return render(request, 'products/add_product.html', {'form': form})

        else:
            form = ProductForm()
            return render(request, 'products/add_product.html', {'form': form})
    return HttpResponse("You do not have permission to add product")