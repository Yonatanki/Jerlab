from django import forms
from django.forms import ModelForm, DateField, widgets
from .models import ADC, Router

# from .utils import DatePickerInput


class AlteonForm(ModelForm):
    class Meta:
        model = ADC

        # widgets = {
        #     'Date': widgets.DateInput(attrs={'type': 'date'})
        # }
        fields = '__all__'
        # widgets = {
        #     'tags':forms.CheckboxSelectMultiple(),
        # }
        # {'date_time': DatePickerInput()}
        # fields = ['MAC', Plateform', ....]

    def __init__(self, *args, **kwargs):
        super(AlteonForm, self).__init__(*args, **kwargs)
        # self.fields['MAC'].widget.attrs.update({'class': 'input'})
        #       loop "for" to styling the form fields in html:
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class RouterForm(ModelForm):
    class Meta:
        model = Router
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RouterForm, self).__init__(*args, **kwargs)
        #       loop "for" to styling the form fields in html:
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
