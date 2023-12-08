import datetime
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Customer(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name='First name'
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Last name'
    )
    phone = models.CharField(
        max_length=15,
        verbose_name='Phone'
    )
    email = models.EmailField(
        max_length=100,
        verbose_name='Email'
    )
    password = models.CharField(
        max_length=100,
        verbose_name='Password'
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'Customers'


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Name'
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        verbose_name='Price'
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        default=1,
        verbose_name='Category'
    )
    description = models.TextField(
        default='',
        blank=True,
        null=True,
        verbose_name='Description'
    )
    image = models.ImageField(
        upload_to='uploads/product',
        verbose_name='Image'
    )
    is_sale = models.BooleanField(
        default=False,
        verbose_name='Is on sale'
    )
    sale_price = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        blank=True,
        null=True,
        verbose_name='Sale price'
    )
    

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Products'


class Order(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='Product'
    )
    customer = models.ForeignKey(
        to=Customer,
        on_delete=models.CASCADE,
        verbose_name='Customer'
    )
    quantity = models.IntegerField(
        default=1,
        verbose_name='Quantity'
    )
    address = models.CharField(
        max_length=200,
        verbose_name='Address'
    )
    phone = models.CharField(
        max_length=15,
        default='',
        blank=True,
        null=True,
        verbose_name='Phone'
    )
    date = models.DateField(
        auto_created=True,
        verbose_name='Date'
    )
    status = models.BooleanField(
        default=False,
        verbose_name='Status'
    )

    def __str__(self) -> str:
        return f'{self.product} - {self.customer}'

    class Meta:
        verbose_name_plural = 'Orders'
