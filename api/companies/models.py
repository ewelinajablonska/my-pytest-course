from django.db import models
from django.forms import URLField
from django.utils.timezone import now

# Create your models here.


class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        LAYOFFS = "Layoffs"
        HIRING_FREEZE = "Hiring_freeze"
        HIRING = "Hiring"

    name = models.CharField(max_length=40, unique=True)
    status = models.CharField(
        max_length=30, choices=CompanyStatus.choices, default=CompanyStatus.HIRING
    )
    last_update = models.DateTimeField(default=now, editable=True)
    aplication_link = models.URLField(blank=True)
    notes = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
