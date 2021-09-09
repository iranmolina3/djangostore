from django.db import models

# Create your models here.

class product(models.Model):
    pk_product = models.AutoField('identificador', primary_key=True, blank=False, null=False)
    name = models.CharField('nombre', max_length=100, blank=False, null=False)
    description = models.TextField('descripcion', blank=False, null=False)
    price = models.DecimalField('precio', max_digits=10, decimal_places=2, blank=False, null=False, default=0.00)
    image1 = models.URLField(max_length=1000, default='https://i.postimg.cc/NMdGGd18/imagen-lista-producto-sin-foto-2-25fa77.png', blank=False, null=False)
    image2 = models.URLField(max_length=1000, default='https://i.postimg.cc/NMdGGd18/imagen-lista-producto-sin-foto-2-25fa77.png', blank=False, null=False)
    discount = models.IntegerField('descuento', blank=False, null=False, default=0)

class purchase(models.Model):
    pk_purchase = models.AutoField('identificador', primary_key=True, blank=False, null=False)
    amount = models.IntegerField('cantidad', blank=False, null=False)
    date_purchase = models.DateField('fecha compra', auto_now=False, auto_now_add=True)
    fk_product = models.ForeignKey(product, blank=False, null=False, on_delete=models.CASCADE)

class client(models.Model):
    pk_client = models.AutoField('identificador', primary_key=True, blank=False, null=False)
    nombre = models.CharField('nombre', max_length=50, blank=False, null=False)
    apellido = models.CharField('nombre', max_length=50, blank=False, null=False)
    telefono = models.CharField('nombre', max_length=8, blank=False, null=False)
    direccion = models.CharField('nombre', max_length=100, blank=False, null=False)

class sale(models.Model):
    pk_sale = models.AutoField('identificador', primary_key=True, blank=False, null=False)
    amount = models.IntegerField('cantidad', blank=False, null=False)
    state = models.BooleanField('cantidad', blank=False, null=False, default=True)
    fk_client = models.ForeignKey(client, blank=False, null=False, on_delete=models.CASCADE)
    fk_product = models.ForeignKey(product, blank=False, null=False, on_delete=models.CASCADE)