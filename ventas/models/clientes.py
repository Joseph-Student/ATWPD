from django.db import models


# Clientes
class Clientes(models.Model):
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = 'Clientes'


    # Denominación del Cliente [VARCHAR]
    denomcliente = models.CharField(verbose_name='Denominación del Cliente', max_length=200, null=False, blank=False, db_column='DenomCliente', )
    # Descripción del Cliente [TEXT]
    desccliente = models.TextField(verbose_name='Descripción del Cliente', null=True, blank=True, db_column='DescCliente', )
    # Fecha de Registro [DATE]
    fecharegistro = models.DateTimeField(verbose_name='Fecha de Registro', null=True, blank=True, db_column='FechaRegistro', )
    # Cliente Activo [CHAR]
    clienteactivo = models.CharField(verbose_name='Cliente Activo', max_length=1, null=False, blank=False, db_column='ClienteActivo', )

    def __str__(self):
        return self.denomcliente
