from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ventas import forms
from ventas.models.articulos import Articulos
from ventas.models.clientes import Clientes
from ventas.models.detventas import DetVentas


# Vistas de Articulos
class ArticuloListView(ListView):
    template_name = 'ventas/articulo/_list.html'
    paginate_by = 10
    model = Articulos


class ArticuloDetailView(DetailView):
    template_name = 'ventas/articulo/_detail.html'
    model = Articulos


class ArticuloCreateView(CreateView):
    template_name = 'ventas/articulo/_form.html'
    form_class = forms.ArticuloForm
    model = Articulos
    extra_context = {
        'submit': 'Registrar'
    }


class ArticuloUpdateView(UpdateView):
    template_name = 'ventas/articulo/_form.html'
    form_class = forms.ArticuloForm
    model = Articulos
    extra_context = {
        'submit': 'Actualizar'
    }


class ArticuloDeleteView(DeleteView):
    template_name = 'ventas/articulo/_delete.html'
    success_url = reverse_lazy('ventas:articulo-list')
    model = Articulos


# Vistas de Clientes
class ClienteListView(ListView):
    template_name = 'ventas/cliente/_list.html'
    paginate_by = 10
    model = Clientes


class ClienteDetailView(DetailView):
    template_name = 'ventas/cliente/_detail.html'
    model = Clientes


class ClienteCreateView(CreateView):
    template_name = 'ventas/cliente/_form.html'
    form_class = forms.ClienteForm
    model = Clientes
    extra_context = {
        'submit': 'Registrar'
    }


class ClienteUpdateView(UpdateView):
    template_name = 'ventas/cliente/_form.html'
    form_class = forms.ClienteForm
    model = Clientes
    extra_context = {
        'submit': 'Actualizar'
    }


class ClienteDeleteView(DeleteView):
    template_name = 'ventas/cliente/_delete.html'
    success_url = reverse_lazy('ventas:cliente-list')
    model = Clientes


# Vistas de Detalles de Ventas
class DetVentaListView(ListView):
    template_name = 'ventas/detventa/_list.html'
    paginate_by = 10
    model = DetVentas


class DetVentaDetailView(DetailView):
    template_name = 'ventas/detventa/_detail.html'
    model = DetVentas


class DetVentaCreateView(CreateView):
    template_name = 'ventas/detventa/_form.html'
    form_class = forms.DetVentasForm
    model = DetVentas
    extra_context = {
        'submit': 'Registrar'
    }


class DetVentaUpdateView(UpdateView):
    template_name = 'ventas/detventa/_form.html'
    form_class = forms.DetVentasForm
    model = DetVentas
    extra_context = {
        'submit': 'Actualizar'
    }


class DetVentaDeleteView(DeleteView):
    template_name = 'ventas/detventas/_delete.html'
    success_url = reverse_lazy('ventas:detventas-list')
    model = DetVentas
