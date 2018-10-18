from django import forms

from ventas.models.articulos import Articulos
from ventas.models.clientes import Clientes
from ventas.models.detventas import DetVentas
from ventas.models.ventasdiarias import VentasDiarias


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = '__all__'
        widgets = {
            'denomarticulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Denominación del Artículo'
                }
            ),
            'descarticulo': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripción del Artículo'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Precio'
                }
            ),
            'existencia': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Existencia'
                }
            ),
            'tipoarticulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Tipo de Artículo'
                }
            )
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'
        widgets = {
            'denomcliente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Denominación del Cliente'
                }
            ),
            'desccliente': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripción del Cliente'
                }
            ),
            'fecharegistro': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'DD/MM/YYYY HH:MM:SS'
                }
            ),
            'clienteactivo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Cliente Activo'
                }
            )
        }


class VentaForm(forms.ModelForm):
    class Meta:
        model = VentasDiarias
        exclude = ['anulada', 'guardada']
        widgets = {
            'numerofactura': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Número de Factura'
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'DD/MM/YYYY'
                }
            ),
            'hora': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'HH:MM:SS'
                }
            ),
            'idcliente': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Cliente'
                }
            ),
            'totalarticulos': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Total Artículos',
                    'readonly': 'readonly'
                }
            ),
            'totalfactura': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Total Factura',
                    'readonly': 'readonly'
                }
            )
        }


class DetVentaInlineForm(forms.ModelForm):
    class Meta:
        model = DetVentas
        fields = '__all__'
        widgets = {
            'cantidad': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Cantidad',
                    'onBlur': 'totalArt()'
                }
            ),
            'idarticulo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Articulo',
                    'onchange': 'precioData(this)'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Precio',
                    'readonly': 'readonly'
                }
            ),
            'monto': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Monto',
                    'readonly': 'readonly'
                }
            )
        }

    class Media:
        css = {
            'all': (
                'ventas/footable-bootstrap.latest/css/footable.bootstrap.min.css',
                'ventas/css/ventas.css',
            )
        }
        js = (
            'ventas/js/venta.js',
            'ventas/footable-bootstrap.latest/js/footable.min.js',
            'ventas/js/footable.js',
        )
