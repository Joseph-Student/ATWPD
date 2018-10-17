from django import forms
from ventas.models.articulos import Articulos
from ventas.models.clientes import Clientes
from ventas.models.detventas import DetVentas


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


class DetVentasForm(forms.ModelForm):
    class Meta:
        model = DetVentas
        fields = '__all__'
