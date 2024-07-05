from django.shortcuts import render, get_object_or_404, redirect
from webapp.models.category_model import Category
from webapp.models.product_model import Product


def products_view(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def product_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "product.html", {"product": product})

def product_add_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        price = request.POST.get('price')
        image = request.POST.get('image')
        category = get_object_or_404(Category, id=category_id)
        product = Product.objects.create(name=name, description=description, price=price, image=image, category=category)
        return redirect('product_view', id=product.id)
    else:
        categories = Category.objects.all()
        return render(request, "product_add_view.html", {"categories": categories})


def product_edit_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        category_id = request.POST.get('category')
        product.category = get_object_or_404(Category, id=category_id)
        product.price = request.POST.get('price')
        product.image = request.POST.get('image')
        product.save()
        return redirect('product_view', id=product.id)
    else:
        categories = Category.objects.all()
        return render(request, "product_edit_view.html", {"product": product, "categories": categories})


def category_add_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        Category.objects.create(name=name, description=description)
        return redirect("categories_view")
    else:
        return render(request, "category_add_view.html")


def categories_view(request):
    categories = Category.objects.all()
    return render(request, "categories_vies.html", {"categories": categories})


def category_edit_view(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        category.name = request.POST["name"]
        category.description = request.POST["description"]
        category.save()
        return redirect("categories_view")
    else:
        return render(request, "category_edit_view.html", {"category": category})


def category_delete_view(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect("categories_view")


def product_delete_view(request, id):
    if request.method == "GET":
        product = get_object_or_404(Product, id=id)
        return render(request, "product_delete.html", {"product": product})
    else:
        product = get_object_or_404(Product, id=id)
        product.delete()
        return redirect("products_view")
