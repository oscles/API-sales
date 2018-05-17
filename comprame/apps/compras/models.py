from django.db import models
from django.db.models import Sum
from django.db.models.expressions import ExpressionWrapper, F
from django.forms.fields import FloatField
from comprame.apps.compras.mixins import TimeStampedModel


class Client(TimeStampedModel):
    email = models.EmailField()
    details = models.TextField(blank=True, null=True)


class Product(TimeStampedModel):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    tags = models.TextField(blank=True, null=True)


class Purchase(TimeStampedModel):
    client = models.ForeignKey(Client)
    products = models.ManyToManyField(Product, through='PurchaseItem')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=15)

    def get_total(self):
        total = PurchaseItem.objects.filter(purchase=self) \
            .annotate(
            subtotal=ExpressionWrapper(
                Sum(F('price') * F('quantity')), output_field=FloatField()
            )).aggregate(total=Sum('subtotal'))
        return total['total']


class PurchaseItem(TimeStampedModel):
    purchase = models.ForeignKey(Purchase)
    product = models.ForeignKey(Product)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    state = models.CharField(max_length=50)
