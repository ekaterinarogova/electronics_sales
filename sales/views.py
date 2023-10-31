from rest_framework import generics
from rest_framework.filters import SearchFilter

from sales.models import Company
from sales.serializers import CompanySerializer, CompanyUpdateSerializer


class CompanyCreateAPIView(generics.CreateAPIView):
    serializer_class = CompanySerializer


class CompanyListAPIView(generics.ListAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']


class CompanyRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CompanyUpdateSerializer
    queryset = Company.objects.all()


class CompanyDeleteAPIView(generics.DestroyAPIView):
    queryset = Company.objects.all()