from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from .constants import PART_DESCRIPTION, OPERATIONS
from django.urls import reverse


class Customer(models.Model):
    CUSTOMERS = (
        ('McLaren', 'McLaren'),
        ('Ferrari', 'Ferrari'),
        ('Morgan', 'Morgan'),
        ('Maserati', 'Maserati'),
    )
    customer = models.CharField(max_length=120, choices=CUSTOMERS, default='Customer')

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('customer-detail', args=[str(self.id)])

    def __str__(self):
        return self.customer


class Part(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    FGcode = models.CharField(max_length=10)

    class Meta:
        ordering = ['FGcode']

    def description(self):
        description_text = [fg[0] for fg in PART_DESCRIPTION if fg[1] == str(self.FGcode)]
        return description_text[0]

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('part-detail', args=[str(self.id)])

    def __str__(self):
        return self.FGcode


class PartInstance(models.Model):
    job_wallet = models.ForeignKey('Wallet', related_name='wallet_parts', on_delete=models.CASCADE, null=True)
    part_origin = models.ForeignKey(Part, related_name='parts', on_delete=models.CASCADE, null=True)
    serial_number = models.CharField(max_length=11)

    class Meta:
        ordering = ['serial_number']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('partinstance-detail', args=[str(self.id)])

    def __str__(self):
        return self.serial_number


class Operation(models.Model):
    owner = models.ForeignKey('auth.User', related_name='operations', on_delete=models.CASCADE, default=1)
    processed_part = models.ForeignKey(PartInstance, related_name='operations', on_delete=models.CASCADE, null=True)
    operation_name = models.CharField(max_length=120, choices=OPERATIONS, unique=True)
    date_signed = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(null=True,  blank=True, max_length=240 )
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    STATUS = (('Passed', 'Passed'), ('Scrapped', 'Scrapped'), ('Quarantined', 'Quarantined'))
    operation_status = models.CharField(max_length=120, choices=STATUS, default='What is the part status?')

    class Meta:
        ordering = ['operation_name']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('operation-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.operation_name

    def save(self, *args, **kwargs):
        super(Operation, self).save(*args, **kwargs)


class Wallet(models.Model):
    order_number = models.CharField(max_length=7)
    order_quantity = models.IntegerField(verbose_name='quantity', default=0)
    customer_name = models.ForeignKey(Customer, related_name='wallets', on_delete=models.CASCADE, null=True)
    part_FG = models.ForeignKey(Part, related_name='part_fgs', on_delete=models.CASCADE, null=True)
    part_id = models.CharField(max_length=120, default='')
    pack_number = models.CharField(max_length=10)
    traceability_required = models.BooleanField(default=True)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('wallet-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.order_number




