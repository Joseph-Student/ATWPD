from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from ventas.models.articulos import Articulos
from ventas.models.clientes import Clientes
from ventas.models.detventas import DetVentas
from ventas import forms


class ArticuloListView(ListView):
    template_name = 'ventas/articulo/_list.html'
    paginate_by = 10
    model = Articulos


class ArticuloCreateView(CreateView):
    template_name = 'ventas/articulo/_form.html'
    form_class = forms.ArticuloForm
    model = Articulos
    extra_context = {
        'submit': 'Registrar'
    }


class ClienteListView(ListView):
    template_name = 'ventas/cliente/_list.html'
    paginate_by = 10
    model = Clientes


class DetVentasListView(ListView):
    template_name = 'ventas/detventa/_list.html'
    paginate_by = 10
    model = DetVentas

