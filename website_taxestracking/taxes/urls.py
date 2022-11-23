from django.urls import path
from taxes.views import *

urlpatterns = [
    path('', form, name='formTaxes'),
]
