import json
from django import views
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Company

# Create your views here.

#Esta clase es la que me ayuda a convertir en una vista para procesar 
# nuestras vistas

class CompanyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def get(self, request, company_id = None):
        
        if company_id == None:
            companies = list(Company.objects.values())
            if len(companies) > 0:
                datos = {
                    'message':'Existen registros',
                    'companies':companies
                }
            else:
                datos = {
                    'message':'No existen registros'
                }
        else:
            companies = list(Company.objects.filter(id = company_id).values())        
            if len(companies) > 0:
                
                datos = {
                    'message':'Existen registros',
                    'companies':companies[0]
                }
            else:
                datos = {
                    'message':'No existe la compañia buscada'
                }
                
        return JsonResponse(datos)
    
    def post(self,request):
        
        json_data = json.loads(request.body)
        
        print(json_data)
        #ingreso esos valores por medio de object create de la ORM
        
        Company.objects.create(nombre = json_data['nombre'],
                               web = json_data['web'],
                               found = json_data['foundation'],
                               city = json_data['city'])
        
        datos = {
            'message':'Registro creado'
        }
        
        return JsonResponse(datos)
        
        datos= {
            'message':'Registro creado',
        }
        return JsonResponse(datos)
        
        
    def put(self,request,company_id):
        
        json_data = json.loads(request.body)
        
        company =list(Company.objects.filter(id = company_id).values())
        
        if len(company) > 0:   
            company = Company.objects.get(id = company_id)
             
            company.nombre = json_data['nombre']
            company.web = json_data['web']
            company.found = json_data['foundation']
            company.city = json_data['city']
            
            company.save()
        
            datos = {
                'message':'Registro actualizado'
            }
            
        else:
            datos = {
                'message':'No existe la compañia buscada'
            }
            
        
        return JsonResponse(datos)
    def delete(self,request,company_id):

        companies = list(Company.objects.filter(id = company_id).values())
        
        if len(companies) > 0:
            
            company = Company.objects.get(id = company_id).delete()
            
            datos = {
                'message':'Registro eliminado'
            }
        else:
            datos = {
                'message': 'No existe la compañia buscada'
            }
        
        return JsonResponse(datos)
