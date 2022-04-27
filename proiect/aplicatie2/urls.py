from django.urls import path
from aplicatie2 import views

app_name = 'companies'

urlpatterns = [
    path('adaugare/', views.CreateCompanyView.as_view(), name='add'),
    path('', views.CompanyView.as_view(), name='list'),
    path('<int:pk>/delete', views.delete_company, name='delete'),
    path('<int:pk>/update', views.UpdateCompanyView.as_view(), name='modify'),
    path('<int:pk>/activate', views.activate_company, name='activate'),
    path('inactive_companies', views.CompaniesInactiveView.as_view(), name='inactive'),
]