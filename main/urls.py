from django.urls import include, path
from django.conf.urls import url
from . import views
from Request.views import show, update_performer

# это нужно, чтобы django понимал какую именно страницу "showSpecificNews" использовать(при наличии страницы с таким же названием в другом application)
app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('login/authorize/', views.authorize, name='authorize'),
    path('<int:id>/', show, name='showRequest'),
    path('<int:id>/update_performer/', update_performer, name='update_performer'),
    #path('<int:id>/', performer_page, name='performer_page'), #performer
]