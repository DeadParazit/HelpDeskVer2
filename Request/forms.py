from django import forms
from django.forms.widgets import *
from main.models import Type_Of_Request, Employee, Request
from django.contrib import admin

class AddRequest(forms.ModelForm):
    # author = forms.ModelMultipleChoiceField(
    #                                     queryset=Employee.objects.all()
    #                                     )


    # status = forms.ModelMultipleChoiceField(queryset=Request.objects.all(), to_field_name="status")
    # applicant_is_notified = forms.BooleanField()
    # performer_is_notified = forms.BooleanField()
    # operator_is_notified = forms.BooleanField()
    # storage = forms.BooleanField()
    #
    #
    #
    # applicant = forms.ModelChoiceField(
    #                                     queryset=Employee.objects.all()
    #                                     )
    # room = forms.IntegerField()
    # building = forms.CharField()
    #
    #
    #
    # way_to_treat = forms.ModelMultipleChoiceField(queryset=Request.objects.all(), to_field_name="way_to_treat")
    # type_of_request = forms.ModelMultipleChoiceField(queryset=Request.objects.all(), to_field_name="type_of_request") #Тип заявки
    #
    #
    #
    # # Тип заявления
    # type = forms.ModelChoiceField(
    #     queryset=Type_Of_Request.objects.all()
    # )
    # priority = forms.ModelMultipleChoiceField(queryset=Request.objects.all(), to_field_name="priority")
    # description = forms.CharField()
    # file = forms.FileField()

    class Meta:
        model = Request
        fields = ('author',
                  'status',
                  'applicant_is_notified',
                  'performer_is_notified',
                  'operator_is_notified',
                  'storage',
                  'applicant',
                  'room',
                  'building',
                  'way_to_treat',
                  'type_of_request',
                  'type',
                  'priority',
                  'description',
                  'file')
        widgets = {
            'status': Select(attrs={'class': 'variable-input', 'placeholder': 'Выберите статус'}),
            'way_to_treat': Select(attrs={'class': 'variable-input', 'placeholder': 'Выберите способ обращения'}),
            'type_of_request': Select(attrs={'class': 'variable-input', 'placeholder': 'Выберите тип заявления'}),
            'priority': Select(attrs={'class': 'variable-input', 'placeholder': 'Выберите приоритет'}),
            'applicant': Select(attrs={'class': 'variable-input', 'placeholder': 'Выберите заявителя', 'id': 'applicant_select'}),
            'type': Select(attrs={'class': 'variable-input', 'placeholder': 'Выберите тип заявки'}),
            'applicant_is_notified': CheckboxInput(attrs={'class': 'discret variable-input checkbox'}),
            'performer_is_notified': CheckboxInput(attrs={'class': 'discret variable-input checkbox'}),
            'operator_is_notified': CheckboxInput(attrs={'class': 'discret variable-input checkbox'}),
            'storage': CheckboxInput(attrs={'class': 'variable-input checkbox'}),
            'room': NumberInput(attrs={'class': 'variable-input'}),
            'building': TextInput(attrs={'class': 'variable-input'}),
            'description': Textarea(attrs={'style': 'resize:none', 'rows': '9', 'cols': '65', 'style': 'resize:none'}),
        }
