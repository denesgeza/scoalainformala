from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from aplicatie2.models import Companies

# Create your views here.


class CompanyView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/companies_index.html'

    def get_context_data(self):
        data = super(CompanyView, self).get_context_data()
        data['companies_list'] = self.model.objects.filter(active=1)
        return data


class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = Companies
    fields = ['name', 'website', 'company_type', 'active']
    template_name = 'aplicatie2/create_company_form.html'

    def get_success_url(self):
        return reverse('companies:list')


class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = ['name', 'website', 'company_type', 'active']
    template_name = 'aplicatie2/create_company_form.html'

    def get_success_url(self):
        return reverse('companies:list')


class CompaniesInactiveView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/companies_index.html'

    def get_context_data(self):
        data = super(CompaniesInactiveView, self).get_context_data()
        data['companies_list'] = self.model.objects.filter(active=0)
        return data


@login_required
def delete_company(request, pk):
    Companies.objects.filter(id=pk).update(active=0)
    return redirect('companies:list')


@login_required
def activate_company(request, pk):
    Companies.objects.filter(id=pk).update(active=1)
    return redirect('companies:list')