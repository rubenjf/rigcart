
from django_filters.widgets import RangeWidget
import django_filters
import django_filters.widgets
from .models import Event


class EventFilter(django_filters.FilterSet):
    _CHOICES = {
    ('Active', 'Active'),
    ('Archieve', 'Archieve')

    }
    rig_date = django_filters.DateFromToRangeFilter(label='Search For  Events  Between Date Range',widget=RangeWidget(attrs={'type': 'date'}))
    rig_choices = django_filters.ChoiceFilter(label='Status',field_name='rig_choices',choices=_CHOICES,initial='Active')
    
    class Meta:
        model = Event
        fields = ['name','location','rig_choices','rig_date']



