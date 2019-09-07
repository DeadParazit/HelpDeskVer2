from django.contrib import admin
from .models import Department,Type_Of_Request,Employee, Request

admin.site.register(Request)
admin.site.register(Department)
admin.site.register(Type_Of_Request)
admin.site.register(Employee)