from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView, BaseDetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ventas import forms
from ventas.models.articulos import Articulos
from ventas.models.clientes import Clientes
from ventas.models.detventas import DetVentas
from ventas.models.ventasdiarias import VentasDiarias
from ventas.utils import BaseInlineModelFormMixin, JSONResponseMixin


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


# Vistas de Ventas Diarias
class BaseVenta(BaseInlineModelFormMixin):
    template_name = 'ventas/venta/_form.html'
    form_class = forms.VentaForm
    model = VentasDiarias

    def get_inline_detalle_class(self):
        self.inline_detalle_class = inlineformset_factory(
            self.model,
            DetVentas,
            form=forms.DetVentaInlineForm,
            extra=0,
            min_num=1
        )

    def get_context_data(self, **kwargs):
        context = {}

        if 'detalle_inlineformset' not in kwargs:
            self.get_inline_detalle_class()
            context['detalle_inlineformset'] = self.get_form_inline(
                self.inline_detalle_class)
        context.update(kwargs)
        return super().get_context_data(**context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.get_inline_detalle_class()
        detalle_inlineformset = self.get_form_inline(self.inline_detalle_class)

        if form.is_valid() and detalle_inlineformset.is_valid():
            return self.form_valid(form, detalle_inlineformset)
        else:
            return self.form_invalid(form, detalle_inlineformset)

    def form_valid(self, form, detalle_inlineformset):
        self.object = form.save()
        detalle_inlineformset.instance = self.object
        self.inline_detalle_object = detalle_inlineformset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, detalle_inlineformset):
        kwargs = {
            'form': form,
            'detalle_inlineformset': detalle_inlineformset
        }
        return self.render_to_response(self.get_context_data(**kwargs))


class VentaListView(ListView):
    template_name = 'ventas/venta/_list.html'
    paginate_by = 10
    model = VentasDiarias


class VentaDetailView(DetailView):
    template_name = 'ventas/venta/_detail.html'
    model = VentasDiarias


class VentaCreateView(BaseVenta, CreateView):
    extra_context = {
        'submit': 'Registrar'
    }

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)


class VentaUpdateView(BaseVenta, UpdateView):
    extra_context = {
        'submit': 'Actualizar'
    }

    def get_form_inline_kwargs(self):
        kwargs = super().get_form_inline_kwargs()

        if hasattr(self, 'object'):
            kwargs.update({
                'instance': self.object
            })
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form, detalle_inlineformset):
        self.object = form.save()
        self.inline_detalle_object = detalle_inlineformset.save()
        return HttpResponseRedirect(self.get_success_url())


class VentaDeleteView(DeleteView):
    template_name = 'ventas/venta/_delete.html'
    success_url = reverse_lazy('ventas:venta-list')
    model = VentasDiarias


class ArticuloAjaxView(JSONResponseMixin, BaseDetailView):
    model = Articulos

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        cantidad = int(request.GET.get('cantidad', '1'))
        data = {
            'precio': self.object.precio,
            'monto': cantidad * self.object.precio
        }
        return self.render_to_response(data)

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)
