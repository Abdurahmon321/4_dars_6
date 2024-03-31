from django.shortcuts import render, redirect
from .models import Car, Category, Color
from .forms import CarForm, CategoryForm, ColorForm
# Create your views here.


def bosh_sahifa(request):
    return render(request, "app/index.html")


def avtomobillar(request):
    cars = Car.objects.all()
    return render(request, "app/avtomobillar.html", {"car": cars})


def kontaktlar(request):
    return render(request, "app/kontaktlar.html")


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/avtomobillar')
    else:
        form = CarForm()
    return render(request, 'app/add_car.html', {'form': form})


def car_detail(request, pk):
    car = Car.objects.filter(pk=pk)
    return render(request, "app/avtomobillar.html", {"car": car})


def car_update_page(request):
    car = Car.objects.all()
    return render(request, "app/car_update.html", {"car": car})


def car_update(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect("avtomobillar")
    else:
        form = CarForm(instance=car)
    return render(request, "app/add_car.html", {"form": form})


def car_delete_page(request):
    car = Car.objects.all()
    return render(request, "app/car_delete_page.html", {"car": car})


def car_delete(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect("avtomobillar")
    context = {
        "car": car
    }
    return render(request, "app/car_delete.html", context)


def category_d(request):
    category = Category.objects.all()
    return render(request, "category/category_detail.html", {"category": category})


def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("category_d")
    else:
        form = CategoryForm
    return render(request, "category/category_create.html", {"form": form})


def category_update(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_d")
    else:
        form = CategoryForm(instance=category)
    return render(request, "category/category_create.html", {"form": form})


def category_delete_page(request):
    category = Category.objects.all()
    return render(request, "category/category_delete_page.html", {"category": category})


def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect("category_d")
    return render(request, "category/category_delete.html", {"category": category})


def color_d(request):
    color = Color.objects.all()
    return render(request, "color/color_detail.html", {"color": color})


def color_create(request):
    if request.method == "POST":
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("color_detail")
    else:
        form = ColorForm()
    return render(request, "color/color_create.html", {"form": form})


def color_update(request, pk):
    color = Color.objects.get(pk=pk)
    if request.method == "POST":
        form = ColorForm(request.POST, instance=color)
        if form.is_valid():
            form.save()
            return redirect("color_detail")
    else:
        form = ColorForm(instance=color)
    return render(request, "color/color_create.html", {"form": form})


def color_delete(request, pk):
    color = Color.objects.get(pk=pk)
    if request.method == "POST":
        color.delete()
        return redirect("color_list")
    return render(request, "color/color_delete.html", {"color": color})

def color_delete_page(request):
    color = Color.objects.all()
    return render(request, "color/color_delete_page.html", {"color": color})