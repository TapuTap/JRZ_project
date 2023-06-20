from typing import Any, Optional, Type
from django.utils.translation import gettext_lazy as _
from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404
from django.views import generic
from . models import Application, ApplicationInstance
from django.db.models import Q
from . forms import ApplicationInstanceForm
from django.urls import reverse, reverse_lazy
from django import forms

def index(request):
    return render(request, 'hr_system/index.html')

def about_us(request):
    return render(request, 'hr_system/about_us.html')

class ApplicationListView(generic.ListView):
    model = Application
    template_name = 'hr_system/application_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            qs = qs.filter(
                Q(id__icontains=query),
                Q(tempalte__icontains=query),
                Q(date_created__icontains=query),
                Q(status__icontains=query)                      
            )
        return qs
    
class ApplicationFormView(generic.CreateView):
    model = ApplicationInstance
    form_class = ApplicationInstanceForm
    template_name = 'hr_system/application_instance.html'
    success_url = reverse_lazy('application_list')

    # Get Aplications object by Application.id(passed throught urls.py)
    def get_application(self):
        return get_object_or_404(Application, pk=self.kwargs['pk'])

    # Create initial form instance populate with needed fields 
    def get_form(self, form_class= form_class) -> BaseModelForm:
        form = super().get_form(form_class)
        
        if self.get_application().title == "Vacation": # Atostogos
            form.fields['start_date'] = forms.DateField(label=_("Start Date"))
            form.fields['end_date'] = forms.DateField(label=_("End Date"))
            form.fields['full_name'] = forms.CharField(label=_("full name"))
            form.fields['manager'] = forms.CharField(label=_("manager"))
            form.fields['payout_before'] = forms.ChoiceField(label=_("Payment"), choices=(
                ("along with the regular salary payment", _("along with the regular salary payment")), 
                ("before requested vacation leave", _("before the requested vacation leave")), ))
        
        if self.get_application().title == "Taxes": # Mokesciai
            form.fields['npd'] = forms.BooleanField(label=_("npd"), required=False)
            form.fields['start_date'] = forms.DateField(label=_("start_date"))
            form.fields['full_name'] = forms.CharField(label=_("full name"))
            form.fields['manager'] = forms.CharField(label=_("manager"))

        if self.get_application().title == "Parent Day-off":
            form.fields['full_name'] = forms.CharField(label=_("full name"))
            form.fields['manager'] = forms.CharField(label=_("manager"))
            form.fields['start_date'] = forms.DateField(label=_("Start Date"))
            form.fields['parental_status'] = forms.ChoiceField(label=_("Parental Day-off"), choices=(
        ("I am raising 1 child under 12 years old", _("Raising 1 child under 12 years old")),
        ("I am raising 2 or more children under 12 years old", _("Raising 2 or more children under 12 years old")),
        ("I am raising 3 or more children under 12 years old", _("Raising 3 or more children under 12 years old")),
        ("I am raising 1 child with disabilities", _("Raising 1 child with disabilities")),
        ("I am raising 2 or more children with disabilities", _("Raising 2 or more children with disabilities"))
        ) )
        
        if self.get_application().title == "Terminate":
            form.fields['full_name'] = forms.CharField(label=_("full name"))
            form.fields['manager'] = forms.CharField(label=_("manager"))
            form.fields['start_date'] = forms.DateField(label=_("Start Date"))
        return form

    # gets populated form, passes throught generate_description() returns form with values
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.application = self.get_application()
        instance.save()
        
        form.instance.content = self.generate_description(form.cleaned_data)
        return super().form_valid(form)

    # Populates form with values(user inputs)
    def generate_description(self, form_data):
        form = self.get_form(self.form_class)
        
        template = self.get_application().description

        # Dynamically create multiple variables
        for key in form.fields.keys():

            locals()[key] = form_data[key]
            if key == 'npd':
                if locals()[key] == True:
                    locals()[key] = 'taikyti'
                else:
                    locals()[key] = 'netaikyti'
        #print(locals())
    
        # **locals() syntax, which unpacks the dynamically created variables as keyword arguments.
        description = template.format(**locals())

        return description
    
    
