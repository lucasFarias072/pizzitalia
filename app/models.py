from django.db import models

# Create your models here.
class Base(models.Model):
    created = models.DateTimeField('Data de criação', auto_now_add=True)
    updated = models.DateTimeField('Última atualização', auto_now=True)
    availability = models.BooleanField('Disponibilidade', default=True)

    class Meta:
        abstract = True

class Costumer(models.Model):
    costumer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=60)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=50)
    signature = models.CharField(max_length=3)
    price_for_medium = models.DecimalField(max_digits=4, decimal_places=2)
    price_for_large = models.DecimalField(max_digits=4, decimal_places=2)
    price_for_oversized = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.label

class ClientOrder(models.Model):
    order_id = models.AutoField(primary_key=True),
    orders_list = models.CharField('Lista do código de cada categoria de pizza', max_length=200)
    sizes_list = models.CharField('Lista do código de cada tamanho de pizza', max_length=100)
    order_bill = models.DecimalField(max_digits=7, decimal_places=2)
    client_owner = models.ForeignKey(Costumer, on_delete=models.CASCADE)
