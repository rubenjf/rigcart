from django import forms
from django.forms import ModelForm
from django import forms
from .models import Event
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField 


class EventForm(ModelForm):
    required_css_class = 'required'
   
    description = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Event
   
        fields  = ['name','location','description','rig_choices','rig_image','document']
        labels = {
            
        }
        widgets = {
            
            'description' : SummernoteWidget(),

        }

class EventForm2(forms.Form):
    content = forms.CharField(widget=SummernoteInplaceWidget())
    