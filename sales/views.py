from rest_framework import generics
from rest_framework.filters import SearchFilter

from sales.models import Company
from sales.serializers import CompanySerializer, CompanyUpdateSerializer


class CompanyCreateAPIView(generics.CreateAPIView):
    """Создает объект :model:`sales.Company` и связанных с ней :model:`sales.Contacts` и :model:`sales.Product`"""
    serializer_class = CompanySerializer


class CompanyListAPIView(generics.ListAPIView):
    """Выводит список объектов :model:`sales.Company`"""
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']


class CompanyRetrieveAPIView(generics.RetrieveAPIView):
    """Выводит один объект :model:`sales.Company`"""
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyUpdateAPIView(generics.UpdateAPIView):
    """Редактирует объект :model:`sales.Company`"""
    serializer_class = CompanyUpdateSerializer
    queryset = Company.objects.all()


class CompanyDeleteAPIView(generics.DestroyAPIView):
    """Удаляет объект :model:`sales.Company`"""
    queryset = Company.objects.all()
