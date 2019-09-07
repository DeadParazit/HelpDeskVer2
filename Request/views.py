from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.template.loader import render_to_string
from main.models import Type_Of_Request, Employee, Request
from .forms import AddRequest
from main.views import main
from django.core import serializers

#Main page
def create(request):
    all_request_types = Type_Of_Request.objects.all()
    all_employers = Employee.objects.all()
    form = AddRequest()
    context = {
        'all_employers': all_employers,
        'all_request_types': all_request_types,
        'form': form,
    }

    return render(request, 'Request/create_document.html', context)

def create_form(request):
    # form = AddRequest(request.POST)
    # if form.is_valid():
    #     # можно написать сразу просто form.save(), но сделав как я сделал сейчас, можно будет менять обьект перед отправкой
    #     request = form.save(commit=False)
    #     request.save()
    # return redirect('main:main')

    all_request_types = Type_Of_Request.objects.all()
    all_employers = Employee.objects.all()
    context = {
        'all_employers': all_employers,
        'all_request_types': all_request_types,
    }
    if request.method == 'POST':
        form = AddRequest(request.POST, request.FILES)
        if form.is_valid():
            request_to_save = form.save(commit=False)
            request_to_save.save()

            redirect('main:main')
    # else:
    #     form = AddRequest()
    #     merged_context = context.copy()
    #     context_to_merge = {
    #         'form': form,
    #     }
    #     merged_context.update(context_to_merge)
    #     context = merged_context
    return main(request)


def show(request,id):

    specific_request = get_object_or_404(Request, pk=id)
    context = {
        'specific_request': specific_request,
    }

    return render(request, 'Request/show_document.html', context)

def show_applicant_ajax(request):
    html = ""
    context = {}
    if request.method == 'GET':
        applicant_id = request.GET.get('applicant_id')

        applicant_set = Employee.objects.filter(pk=applicant_id)

        for applicant in applicant_set:
            phone = applicant.phone
            department = applicant.department

        context = {
            'phone': phone, #Телефон заявителя
            'department_name': department.name, #Название подразделения, где работает заявитель
        }
        if request.is_ajax():
            html = render_to_string('Request/templates/ajax_applicant_data.html', context)
            return HttpResponse(html)
    return HttpResponse(html)


