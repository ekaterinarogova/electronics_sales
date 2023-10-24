from django.db import models
from django.utils import timezone


class Company(models.Model):
    TYPE_CHOICES = (
        ('FA', 'Factory'),
        ('RN', 'Retail network'),
        ('IE', 'Individual entrepreneur')
    )
    title = models.CharField(max_length=200, verbose_name='название')
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, verbose_name='тип поставщика')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,
                                 verbose_name='поставщик', related_name='company')
    debt = models.PositiveIntegerField(verbose_name='задолженность поставщику')
    created_at = models.DateTimeField(verbose_name='время создания', auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.title}"

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'


class Contacts(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='компания', related_name='contacts')
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=150, verbose_name='страна')
    city = models.CharField(max_length=150, verbose_name='город')
    street = models.CharField(max_length=150, verbose_name='улица')
    house = models.CharField(max_length=100, verbose_name='дом')

    def __str__(self):
        return f"{self.email}, {self.country}, {self.street}, {self.city}, {self.street}, {self.house}"

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='компания', related_name='product')
    title = models.CharField(max_length=200, verbose_name='название')
    model = models.CharField(max_length=150, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода продукта', default=timezone.now())

