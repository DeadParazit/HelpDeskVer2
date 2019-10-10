from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.template.loader import render_to_string
from main.models import Type_Of_Request, Employee, Request
from main.forms import  AuthorizeForm

def main(request):
    if 'user_id' not in request.session:
        return redirect('main:login')

    all_requests = Request.objects.all()

    all_formated_date = list()
    for req in all_requests:
        req.time = req.time.strftime("%H:%M")
    context = {
        'all_requests': all_requests,
    }

    return render(request, 'main/main.html', context)

def login(request):
    all_employees = Employee.objects.all()

    context = {
        'all_employees': all_employees,
    }

    return render(request, 'main/authorization.html', context)

def authorize(request):

    form = AuthorizeForm(request.POST)
    if form.is_valid():
        request.session['user_id'] = form.cleaned_data['user_id']
        request.session.set_expiry(0)
    return redirect('main:main')