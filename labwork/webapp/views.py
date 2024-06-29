
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models.category_model import Category
from webapp.models.product_model import Product


def products_view(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def product_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "product.html", {"product": product})


def product_edit_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        category_id = request.POST.get('category_id')
        product.category_id = request.POST.get('category_id')
        product.price = request.POST.get('price')
        product.category_id = request.POST.get('category_id')
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.category = get_object_or_404(Category, category_id)
        product.save()
        return redirect('product_view', pk=product.id)


def category_add_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        Category.objects.create(name=name, description=description)
        return redirect("category_view")


def categories_view(request):
    categories = Category.objects.all()
    return render(request, "categories_vies.html", {"categories": categories})


def category_edit_view(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == "POST":
        category.name = request.POST["name"]
        category.description = request.POST["description"]
        category.save()
        return redirect("category_view", category_id=category_id)
    else:
        return render(request, "category_edit_view.html", {"category": category})

# Create your views here.
