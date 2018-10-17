from django.db import models


# Artículos
class Articulos(models.Model):
    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        db_table = 'Articulos'
        ordering = ['id']


    # Denominación del Artículo [VARCHAR]
    denomarticulo = models.CharField(verbose_name='Denominación del Artículo', max_length=200, null=False, blank=False, db_column='DenomArticulo', )
    # Descripción del Artículo [TEXT]
    descarticulo = models.TextField(verbose_name='Descripción del Artículo', null=True, blank=True, db_column='DescArticulo', )
    # Precio [DECIMAL]
    precio = models.FloatField(verbose_name='Precio', null=True, blank=True, db_column='Precio', )
    # Existencia [DECIMAL]
    existencia = models.FloatField(verbose_name='Existencia', null=True, blank=True, db_column='Existencia', )
    # Tipo de Artículo [VARCHAR]
    tipoarticulo = models.CharField(verbose_name='Tipo de Artículo', max_length=20, null=True, blank=True, db_column='TipoArticulo', )

    def __str__(self):
        return self.denomarticulo
