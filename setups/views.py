from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import (
    Product, AgencyType, RiskClass, RiskType, Schedule, 
    Tariff, DiscountType, BodyType, VehicleMake, VehicleModel
)


# Product Views
class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"


class ProductCreateView(CreateView):
    model = Product
    fields = ['name']
    template_name = "product_form.html"
    success_url = reverse_lazy('product_list')
    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        # Check if the make with the same name already exists
        if VehicleMake.objects.filter(name__iexact=name).exists():
            # Add an error message to the form
            form.add_error('name', 'This Product already exists.')
            return self.form_invalid(form)
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name']   
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name']
    template_name = "product_form.html"
    success_url = reverse_lazy('product_list')


class VehicleMakeListView(ListView):
    model = VehicleMake
    template_name = "make_list.html"


class VehicleMakeCreateView(CreateView):
    model = VehicleMake
    fields = ['name']
    template_name = "make_form.html"
    success_url = reverse_lazy('make-list')
    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        # Check if the make with the same name already exists
        if VehicleMake.objects.filter(name__iexact=name).exists():
            # Add an error message to the form
            form.add_error('name', 'This make already exists.')
            return self.form_invalid(form)
        return super().form_valid(form)


class VehicleMakeUpdateView(UpdateView):
    model = VehicleMake
    fields = ['name']   
    success_url = reverse_lazy('make-list')

class VehicleMakeDeleteView(DeleteView):
    model = VehicleMake
    fields = ['name']
    template_name = 'make_delete.html'   
    success_url = reverse_lazy('make-list')

    
    

# AgencyType Views
class AgencyTypeListView(ListView):
    model = AgencyType
    template_name = "agencytype_list.html"


class AgencyTypeCreateView(CreateView):
    model = AgencyType
    fields = ['name', 'symbol']
    template_name = "agencytype_form.html"
    success_url = reverse_lazy('agencytype_list')


class AgencyTypeUpdateView(UpdateView):
    model = AgencyType
    fields = ['name', 'symbol']
    template_name = "agencytype_form.html"
    success_url = reverse_lazy('agencytype_list')


# RiskClass Views
class RiskClassListView(ListView):
    model = RiskClass
    template_name = "riskclass_list.html"


class RiskClassCreateView(CreateView):
    model = RiskClass
    fields = ['name']
    template_name = "riskclass_form.html"
    success_url = reverse_lazy('riskclass_list')


class RiskClassUpdateView(UpdateView):
    model = RiskClass
    fields = ['name']
    template_name = "riskclass_form.html"
    success_url = reverse_lazy('riskclass_list')


# RiskType Views
class RiskTypeListView(ListView):
    model = RiskType
    template_name = "risktype_list.html"


class RiskTypeCreateView(CreateView):
    model = RiskType
    fields = ['name']
    template_name = "risktype_form.html"
    success_url = reverse_lazy('risktype_list')


class RiskTypeUpdateView(UpdateView):
    model = RiskType
    fields = ['name']
    template_name = "risktype_form.html"
    success_url = reverse_lazy('risktype_list')


# Schedule Views
class ScheduleListView(ListView):
    model = Schedule
    template_name = "schedule_list.html"


class ScheduleCreateView(CreateView):
    model = Schedule
    fields = ['name', 'code', 'usage_type', 'person_entitled_note', 'limitation_note', 'exclusions_note']
    template_name = "schedule_form.html"
    success_url = reverse_lazy('schedule_list')


class ScheduleUpdateView(UpdateView):
    model = Schedule
    fields = ['name', 'code', 'usage_type', 'person_entitled_note', 'limitation_note', 'exclusions_note']
    template_name = "schedule_form.html"
    success_url = reverse_lazy('schedule_list')


# Tariff Views
class TariffListView(ListView):
    model = Tariff
    template_name = "tariff_list.html"


class TariffCreateView(CreateView):
    model = Tariff
    fields = [
        'schedule', 'start_date', 'end_date', 'basic_premium', 'extra_seats', 'additional_peril', 'ecowas_peril', 
        'pa_premium', 'limit', 'sticker_fee', 'brown_card_sticker_fee', 'excess_rate', 'ecowas_peril_delta', 
        'basic_premium_delta', 'minimum_premium', 'comprehensive_min_rate', 'comprehensive_max_rate', 
        'comprehensive_excess_constant', 'third_party_rate', 'third_party_limit', 'third_party_fire_min_rate', 
        'third_party_fire_max_rate'
    ]
    template_name = "tariff_form.html"
    success_url = reverse_lazy('tariff_list')


class TariffUpdateView(UpdateView):
    model = Tariff
    fields = [
        'schedule', 'start_date', 'end_date', 'basic_premium', 'extra_seats', 'additional_peril', 'ecowas_peril', 
        'pa_premium', 'limit', 'sticker_fee', 'brown_card_sticker_fee', 'excess_rate', 'ecowas_peril_delta', 
        'basic_premium_delta', 'minimum_premium', 'comprehensive_min_rate', 'comprehensive_max_rate', 
        'comprehensive_excess_constant', 'third_party_rate', 'third_party_limit', 'third_party_fire_min_rate', 
        'third_party_fire_max_rate'
    ]
    template_name = "tariff_form.html"
    success_url = reverse_lazy('tariff_list')


# DiscountType Views
class DiscountTypeListView(ListView):
    model = DiscountType
    template_name = "discounttype_list.html"



class DiscountTypeCreateView(CreateView):
    model = DiscountType
    fields = ['name', 'risk_class']
    template_name = "discounttype_form.html"
    success_url = reverse_lazy


class BodyTypeCreateView(CreateView):
    model = BodyType
    fields = ['name', 'seats_num']
    template_name = 'bodytype_form.html'
    success_url = reverse_lazy

