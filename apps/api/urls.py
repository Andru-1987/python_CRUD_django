from django.urls import path
from .views import CompanyView


urlpatterns = [
    # ruta root/ -> endpoint: companies_list
    path('companies/', CompanyView.as_view(), name = 'companies_list'),
    path('companies/<int:company_id>', CompanyView.as_view(), name = 'company_process'),
    ]