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
            'status': Select(attrs={'class': 'requered status status_form', 'placeholder': 'Выберите статус'}),
            'way_to_treat': Select(attrs={'class': 'requered request_from request_form', 'placeholder': 'Выберите способ обращения'}),
            'type_of_request': Select(attrs={'class': 'requered request_type1 request_form', 'placeholder': 'Выберите тип заявления'}),
            'priority': Select(attrs={'class': 'discret request_priority', 'placeholder': 'Выберите приоритет'}),
            'applicant': Select(attrs={'class': 'requered applicant applicant_form', 'placeholder': 'Выберите заявителя', 'id': 'applicant_select'}),
            'type': Select(attrs={'class': 'requered request_type2 request_form2', 'placeholder': 'Выберите тип заявки'}),
            'applicant_is_notified': CheckboxInput(attrs={'class': 'discret applicant_notified checkbox'}),
            'performer_is_notified': CheckboxInput(attrs={'class': 'discret performer_notified checkbox'}),
            'operator_is_notified': CheckboxInput(attrs={'class': 'discret operator_notified checkbox'}),
            'storage': CheckboxInput(attrs={'class': 'variable-input checkbox'}),
            'room': NumberInput(attrs={'class': 'requered cabinet applicant_form'}),
            'building': TextInput(attrs={'class': 'equered location applicant_form'}),
            'description': Textarea(attrs={'style': 'resize:none', 'rows': '9', 'cols': '65', 'class': 'requered request_description request_form2'}),
            'file': FileInput(attrs={'class':'discret applicant_file file'}),
        }
