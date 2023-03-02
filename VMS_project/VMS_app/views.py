from django.shortcuts import render
from .models import Vehicle
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'


@method_decorator(staff_member_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class VehicleCreateView(CreateView):
    model = Vehicle
    fields = '__all__'
    template_name = 'vehicle_form.html'


@method_decorator(login_required, name='dispatch')
class VehicleUpdateView(UpdateView):
    model = Vehicle
    fields = '__all__'
    template_name = 'vehicle_form.html'


@method_decorator(staff_member_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle_list')


class TemplateDeleteView(TemplateView):
    template_name = 'Success.html'


#from .forms import VehicleForm
#from django.urls import reverse_lazy
#from django.views.generic.edit import FormView


#class VehicleFormView(FormView):
    #template_name = 'vehicle_form.html'
    #form_class = VehicleForm
    #success_url = reverse_lazy('vehicle_list')

    #def form_valid(self, form):
        # Call the parent class's form_valid() method to save the form data and
        # redirect to the success URL
       # response = super().form_valid(form)
        # Do something with the validated form data
        #return response
