from django.db import models

# Ventas Diarias
from django.urls import reverse


class VentasDiarias(models.Model):
    class Meta:
        verbose_name = "Venta Diaria"
        verbose_name_plural = "Ventas Diarias"
        db_table = 'VentasDiarias'
        ordering = ['numerofactura', 'fecha']

    # Número de Factura [VARCHAR]
    numerofactura = models.CharField(verbose_name='Número de Factura',
                                     max_length=20, null=False, blank=False,
                                     db_column='NumeroFactura', )
    # Fecha [DATE]
    fecha = models.DateTimeField(verbose_name='Fecha', null=True, blank=True,
                                 db_column='Fecha', )
    # Hora [TIME]
    hora = models.DateTimeField(verbose_name='Hora', null=True, blank=True,
                                db_column='Hora', )
    # Id Cliente [INTEGER]
    idcliente = models.ForeignKey('Clientes', verbose_name='Cliente',
                                  related_name='idcliente_ventasdiarias',
                                  help_text='Seleccione Cliente',
                                  on_delete=models.DO_NOTHING, null=False,
                                  blank=False, db_column='IdCliente', )
    # Anulada [CHAR]
    anulada = models.CharField(verbose_name='Anulada', max_length=1,
                               null=False, blank=False, db_column='Anulada', )
    # Total Artículos [DECIMAL]
    totalarticulos = models.FloatField(verbose_name='Total Artículos',
                                       null=False, blank=False,
                                       db_column='TotalArticulos', )
    # Total Factura [DECIMAL]
    totalfactura = models.FloatField(verbose_name='Total Factura', null=True,
                                     blank=True, db_column='TotalFactura', )
    # Guardada [CHAR]
    guardada = models.CharField(verbose_name='Guardada', max_length=1,
                                null=False, blank=False,
                                db_column='Guardada', )

    def __str__(self):
        return '(VentasDiarias)'

    def get_absolute_url(self):
        return reverse("ventas:venta-detail", kwargs={'pk': self.pk})
