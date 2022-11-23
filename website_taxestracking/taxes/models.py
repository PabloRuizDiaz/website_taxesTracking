from django.db import models
from django.utils.translation import gettext_lazy as _


class taxNameModel(models.Model):
    class categories(models.TextChoices):
        imp_muni = 'muni', _('Impuestos Municipales')
        imp_prov = 'prov', _('Impuestos Provinciales')
        imp_nac = 'naci', _('Impuestos Nacionales')
        serv_pu = 'sepu', _('Servicios Publicos')
        serv_pr = 'sepr', _('Servicios Privados')

    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=4, null=True, blank=True, choices=categories.choices)
    tax = models.CharField(max_length=100, null=True, blank=True, unique=True)

    def __str__(self):
        return f'{self.category} -> {self.tax}'

    class Meta:
        db_table = 'tax_name'


class taxesModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    tax = models.ForeignKey(taxNameModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    money = models.FloatField(null=True, blank=True)
    pay_day = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.tax} -> EN EL DIA -> {self.pay_day}'

    class Meta:
        db_table = 'taxes'
