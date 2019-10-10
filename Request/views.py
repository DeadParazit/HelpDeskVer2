from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.template.loader import render_to_string
from main.models import Type_Of_Request, Employee, Request
from .forms import AddRequest, AddRequestPerformer, AddFeedbackApplicant
import datetime
from main.views import main
from django.core import serializers

#Main page
def create(request):
    if 'user_id' not in request.session:
        return redirect('main:login')

    all_employers = Employee.objects.all()
    form = AddRequest()
    context = {
        'all_employers': all_employers,
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
    if 'user_id' not in request.session:
        return redirect('main:login')

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
            specific_request = Request.objects.last()
            type = Type_Of_Request.objects.filter(pk=specific_request.type.id)
            if(specific_request.priority == '1'):
                specific_request.deadline = datetime.date.today() + datetime.timedelta(1)
            elif(specific_request.priority == '2'):
                specific_request.deadline = datetime.date.today() + datetime.timedelta(3)
            elif (specific_request.priority == '3'):
                specific_request.deadline = datetime.date.today() + datetime.timedelta(7)
            elif (specific_request.priority == '4'):
                specific_request.deadline = datetime.date.today() + datetime.timedelta(14)

            specific_request.performer = type.first().responsible
            specific_request.save()
            return redirect('main:main')
    # else:
    #     form = AddRequest()
    #     merged_context = context.copy()
    #     context_to_merge = {
    #         'form': form,
    #     }
    #     merged_context.update(context_to_merge)
    #     context = merged_context
    return redirect('main:main')

def update_performer(request, id):
    if 'user_id' not in request.session:
        return redirect('main:login')

    specific_request = get_object_or_404(Request, id=id)
    if request.method == 'POST':
        print('request = post')
        form = AddRequestPerformer(request.POST, request.FILES)
        if form.is_valid():
            cleaned_form = form.cleaned_data
            specific_request = get_object_or_404(Request, pk=id)
            specific_request.materials_usage_comment = cleaned_form['materials_usage_comment']
            specific_request.is_new = cleaned_form['is_new']
            specific_request.performer_comment = cleaned_form['performer_comment']
            specific_request.storage_type = cleaned_form['storage_type']
            specific_request.exit_code = cleaned_form['exit_code']
            specific_request.complexity = cleaned_form['complexity']
            specific_request.performer_file = cleaned_form['performer_file']
            specific_request.deadline = cleaned_form['deadline']
            specific_request.status = cleaned_form['status']
            specific_request.performer = cleaned_form['performer']
            specific_request.save()

            print('Form is valid')
            return redirect('main:main')
    print('something is wrong')
    return redirect('main:main')

def show(request,id):
    if 'user_id' not in request.session:
        return redirect('main:login')


    specific_request = get_object_or_404(Request, pk=id)
    if int(request.session['user_id']) == int(specific_request.type.responsible.id): #Зашёл отвечающий за выполнение заявки
        print(str(request.session['user_id']) + ' / ' + str(specific_request.type.responsible.id))
        all_employers = Employee.objects.all()
        form = AddRequestPerformer()
        context = { 
            'specific_request': specific_request,
            'form': form,
        }

        return render(request, 'Request/performer_document.html', context)
    elif int(request.session['user_id']) == int(specific_request.applicant.id):
        notified = 0
        if specific_request.applicant_is_notified == True:
            notified += 1
        if specific_request.performer_is_notified == True:
            notified += 1
        if specific_request.operator_is_notified == True:
            notified += 1
        context = {
            'specific_request': specific_request,
            'notified': notified,
        }

        return render(request, 'Request/applicant_document.html', context)
    else:
        form = AddFeedbackApplicant()
        context = {
            'specific_request': specific_request,
            'form': form,
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

def show_performer_storage_ajax(request):
    html = ""
    context = {}
    if request.method == 'GET':
        form = AddRequestPerformer()
        context = {
            'form': form,
        }
        if request.is_ajax():
            html = render_to_string('Request/templates/show_performer_storage_ajax.html', context)
            return HttpResponse(html)
    return HttpResponse(html)

def show_performer_date_ajax(request):
    html = ""
    context = {}
    if request.method == 'GET':
        form = AddRequestPerformer()
        context = {
            'form': form,
        }
        if request.is_ajax():
            html = render_to_string('Request/templates/show_performer_deadline_ajax.html', context)
            return HttpResponse(html)
    return HttpResponse(html)

# def show_applicant_ajax(request):
#     html = ""
#     context = {}
#     if request.method == 'GET':
#         form = AddRequestPerformer()
#         context = {
#             'form': form,
#         }
#         if request.is_ajax():
#             html = render_to_string('Request/templates/ajax_applicant_data.html', context)
#             return HttpResponse(html)
#     return HttpResponse(html)


