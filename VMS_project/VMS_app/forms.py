from django import forms
from django.core import validators
import re
from .models import Vehicle


#def validate_vehicle_number(value):
    # Example vehicular number for Delhi: DL01AB1234,KA01AB1234
 #   if not value[0:2:1].isupper() and len(value) !=10:
  #      raise forms.ValidationError('Invalid vehicular number')
   # elif not value[2:4:1].isdigit() and len(value) !=10:
    #    raise forms.ValidationError('Invalid vehicular number')
    #elif not value[4:6:1].isupper() and len(value) !=10:
     #   raise forms.ValidationError('Invalid vehicular number')
    #elif not value[6::1].isdigit() and len(value) !=10:
     #   raise forms.ValidationError('Invalid vehicular number')


#class VehicleForm(forms.ModelForm):
 #   vehicle_number = forms.CharField(validators=[validate_vehicle_number])

  #  class Meta:
   #     model = Vehicle
    #    fields = '__all__'
from django import forms

from django.core.validators import RegexValidator

#class VehicleForm(forms.Form):
    #alphanumeric = RegexValidator(r'^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')
    #Vehicle_Number = forms.CharField(max_length=10, validators=[alphanumeric])
    #Vehicle_Type = forms.CharField(max_length=20)
    #Vehicle_Model = forms.CharField(max_length=50)
    #Vehicle_Description = forms.CharField(widget=forms.Textarea)

    #vehicle_number_regex = RegexValidator(
     #   regex=r'^[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}$',
      #  message="Vehicle number should be in the format: MH12CD1234"
    #)
    #Vehicle_Number.validators.append(vehicle_number_regex)
