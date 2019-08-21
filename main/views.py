from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.template.loader import render_to_string
from main.models import Type_Of_Request, Employee, Request

def main(request):
    all_requests = Request.objects.all()
    context = {
        'all_requests': all_requests,
    }

    return render(request, 'main/main.html', context)