from django.db import models
from aplicatie1.models import Location

# Create your models here.
company_choices = (('SRL', 'S.R.L'), ('SA', 'S.A.'), ('II', 'I.I'))


class Companies(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    company_type = models.CharField(max_length=10, choices=company_choices)
    active = models.BooleanField(default=1)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.company_type}'
