from django.contrib import admin
from .models import Department, Role, UserModel

# Register your models here.

admin.site.register(Department)
admin.site.register(Role)
admin.site.register(UserModel)
