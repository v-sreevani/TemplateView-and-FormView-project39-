from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView

from django.views.generic import FormView
from app.forms import *

class cbv_context(TemplateView):
    template_name='cbv_context.html'

    def get_context_data(self, **kwargs) :
        EDCO=super().get_context_data(**kwargs)

        EDCO['name']="Harshad"
        EDCO['age']=28
        return EDCO

class cbv_form(FormView):
    template_name='cbv_form.html'
    form_class=SchoolForm

    def form_valid(self, form):
        form.save()

        return HttpResponse('data is saved')
