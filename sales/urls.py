from sales.apps import SalesConfig
from django.urls import path

from sales.views import CompanyCreateAPIView, CompanyListAPIView, CompanyRetrieveAPIView, CompanyUpdateAPIView, \
    CompanyDeleteAPIView

app_name = SalesConfig.name

urlpatterns = [
    path('create/', CompanyCreateAPIView.as_view(), name='create'),
    path('list/', CompanyListAPIView.as_view(), name='list'),
    path('retrieve/<int:pk>/', CompanyRetrieveAPIView.as_view(), name='retrieve'),
    path('update/<int:pk>/', CompanyUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', CompanyDeleteAPIView.as_view(), name='delete'),
]
