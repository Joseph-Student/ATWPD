from django.db import models


# Detalles de Ventas
class DetVentas(models.Model):
    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalles de Ventas"
        db_table = 'DetVentas'


    # Id Venta [INTEGER]
    idventa = models.ForeignKey('VentasDiarias', verbose_name='Venta', related_name='idventa_detventas', help_text='Seleccione Venta', on_delete=models.DO_NOTHING, null=False, blank=False, db_column='IdVenta', )
    # Cantidad [DECIMAL]
    cantidad = models.FloatField(verbose_name='Cantidad', null=False, blank=False, db_column='Cantidad', )
    # Id Articulo [INTEGER]
    idarticulo = models.IntegerField(verbose_name='Articulo', null=False, blank=False, db_column='IdArticulo', )
    # Precio [DECIMAL]
    precio = models.FloatField(verbose_name='Precio', null=True, blank=True, db_column='Precio', )
    # Monto [DECIMAL]
    monto = models.FloatField(verbose_name='Monto', null=True, blank=True, db_column='Monto', )

    def __str__(self):
        return '(DetVentas)'
