from django.urls import include, path
from django.conf.urls import url
from . import views

# это нужно, чтобы django понимал какую именно страницу "showSpecificNews" использовать(при наличии страницы с таким же названием в другом application)
app_name = 'request'

urlpatterns = [
    path('', views.create, name='createRequest'),
    path('show/', views.show_applicant_ajax, name='show_applicant_ajax'), #show applicant info(ajax, applicant_page.html),
    path('create_document/', views.create_form, name='create_form'),
]