from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.template.loader import render_to_string
from main.models import Type_Of_Request, Employee, Request

#Main page
def create(request):
    all_request_types = Type_Of_Request.objects.all()
    all_employers = Employee.objects.all()
    context = {
        'all_employers': all_employers,
        'all_request_types': all_request_types,
    }

    return render(request, 'Request/create_document.html', context)

def show(request,id):
    all_request_types = Type_Of_Request.objects.all()
    all_employers = Employee.objects.all()
    request = get_object_or_404(Request, pk=id)
    context = {
        'all_employers': all_employers,
        'all_request_types': all_request_types,
        'request': request,
    }

    return render(request, 'Request/create_document.html', context)