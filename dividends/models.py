from django.db import models

class Dividend(models.Model):
    company = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    sector = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    cons_years = models.IntegerField()
    ranking = models.IntegerField()
    drip_fees = models.CharField(null=True, max_length=1)
    spp_fees = models.CharField(null=True, max_length=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    div_yield = models.DecimalField(max_digits=4, decimal_places=2)
    current_dividend = models.DecimalField(max_digits=6, decimal_places=4)
    num_payouts = models.IntegerField()
    annual_dividend = models.DecimalField(max_digits=5, decimal_places=2)
    schedule = models.CharField(max_length=6)
    previous_dividend = models.DecimalField(max_digits=6, decimal_places=2)
    ex_dividend_date = models.DateField()
    payable_date = models.DateField()
    mr_increase = models.DecimalField(max_digits=5, decimal_places=2)
    dgr_1 = models.DecimalField(max_digits=7, decimal_places=3)
    dgr_3 = models.DecimalField(max_digits=7, decimal_places=3)
    dgr_5 = models.DecimalField(null=True, max_digits=7, decimal_places=3)
    dgr_10 = models.DecimalField(null=True, max_digits=7, decimal_places=3)
    ad_5_10 = models.DecimalField(null=True, max_digits=7, decimal_places=3)
    deg_5 = models.DecimalField(null=True, max_digits=7, decimal_places=3)
    eps = models.DecimalField(null=True, max_digits=7, decimal_places=3)
    ttm_pe = models.DecimalField(null=True, max_digits=7, decimal_places=3)
    fye = models.IntegerField()
    def __str__(self):
        return self.company









