from django.db import models


# Create your models here.
from business_api.models import Form, Part, Option


class Customer(models.Model):
    name = models.CharField(max_length=255)

    form = models.ForeignKey(Form, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CustomerChoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    option_selected = models.ForeignKey(Option, on_delete=models.CASCADE)

    text_field = models.CharField(max_length=255, default='text')
    number_field = models.IntegerField(default=0)
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    datetime_field = models.DateTimeField(auto_now_add=True)
    #    file_field = models.FileField()
    date_field = models.DateField(auto_now_add=True)
