from django import forms
from django.forms.widgets import *
from main.models import Request

class AddRequest(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('way_to_treat',
                  'type_of_request',
                  'priority',
                  'applicant',
                  'type',
                  'applicant_is_notified',
                  'performer_is_notified',
                  'operator_is_notified',
                  'storage',
                  'room',
                  'building',
                  'description',
                  'file')
        widgets = {
            # 'status': Select(attrs={'class': 'requered status status_form', 'placeholder': 'Выберите статус'}),
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
            'building': TextInput(attrs={'class': 'requered location applicant_form'}),
            'description': Textarea(attrs={'style': 'resize:none; height:158px', 'rows': '9', 'cols': '65', 'class': 'requered request_description request_form2'}),
            'file': FileInput(attrs={'class':'discret applicant_file file'}),
        }

class AddRequestPerformer(forms.ModelForm):

    class Meta:
        model = Request
        fields = (
                  'materials_usage_comment',
                  'is_new',
                  'performer_comment',
                  'storage_type',
                  'exit_code',
                  'complexity',
                  'performer_file',
                  'deadline',
                  'status',
                  'performer',)
        widgets = {
            # 'materials_usage': CheckboxInput(attrs={'class': 'variable-input checkbox materials_usage_check', 'id': 'materials_usage'}),
            'materials_usage_comment': Textarea(),
            'is_new': CheckboxInput(attrs={'class': 'variable-input checkbox materials_usage_new'}),
            'performer_comment': Textarea(attrs={'rows':'9', 'cols':'65', 'style':'resize:none; height:158'}),
            'storage_type': Select(attrs={'placeholder': 'Выберите способ обращения к складу', 'id':'storage_type'}),
            'exit_code': Select(attrs={'placeholder': 'Выберите код закрытия'}),
            'complexity': Select(attrs={'placeholder': 'Выберите сложность заявки'}),
            'performer_file': FileInput(attrs={'class': 'file'}),
            'deadline': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'status': Select(attrs={'placeholder': 'Выберите статус'}),
            'performer': Select(attrs={'placeholder': 'Выберите исполнителя'}),
            # 'is_date_changed': CheckboxInput(attrs={'class': 'variable-input checkbox'}),
            }

    def __init__(self, *args, **kwargs):
        super(AddRequestPerformer, self).__init__(*args, **kwargs)
        self.fields['materials_usage_comment'].required = False
        self.fields['is_new'].required = False
        self.fields['performer_comment'].required = False

        self.fields['storage_type'].required = False
        self.fields['exit_code'].required = False
        self.fields['complexity'].required = False
        self.fields['performer_file'].required = False

        self.fields['deadline'].required = False
        self.fields['status'].required = False
        self.fields['performer'].required = False


class AddFeedbackApplicant(forms.ModelForm):

    class Meta:
        model = Request
        fields = (
                  'materials_usage_comment',
                  'is_new',)
        widgets = {

            }

