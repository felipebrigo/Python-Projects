from django.urls import reverse_lazy

from .models import Product
from django.shortcuts import render, redirect
from .forms import ProductForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView

# ------- CRUD RECEIVING REQUEST AND ID FROM HTTP --------


def list_products(request):
    allproducts = Product.objects.all()
    return render(request, 'products.html', {'allproducts': allproducts})


@login_required(login_url='login/')
def create_products(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render(request,'products-form.html', {'form': form})


@login_required(login_url='login/')
def update_products(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render(request, 'products-form.html', {'form': form, 'product': product})


@login_required(login_url='login/')
def delete_products(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')
    return render(request, 'prod-delete-confirm.html', {'product': product})


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            messages.error(request, "Usuario ou senha inválidos")
    return redirect('/')


class IndexTemplateView(TemplateView):
    template_name = "index.html"


# ------- CRUD USING PRE-CREATED VIEWS INSIDE DJANGO/PYTHON --------
'''
class ProductCreateView(CreateView):
    template_name = 'products-form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('ProductListView')


class ProductDeleteView(DeleteView):
    template_name = 'prod-delete-confirm.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('ProductListView')


class ProductListView(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'allproducts'

class IndexTemplateView(TemplateView):
    template_name = "index.html"

class ProductUpdateView(UpdateView):
    template_name = 'products-update.html'
    model = Product
    fields = '__all__'
    context_object_name = 'product'
    success_url = reverse_lazy('ProductListView')


    def get_object(self, queryset=None):
        product = None
        id = self.kwargs.get(self.pk_url_kwarg)

        if id is not None:
            # Busca o produto a partir do id
            product = Product.objects.filter(id=id).first()

        return product
'''