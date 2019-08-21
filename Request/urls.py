from django.urls import include, path
from django.conf.urls import url
from . import views

# это нужно, чтобы django понимал какую именно страницу "showSpecificNews" использовать(при наличии страницы с таким же названием в другом application)
app_name = 'main'

urlpatterns = [
    path('', views.create, name='createRequest'),
]