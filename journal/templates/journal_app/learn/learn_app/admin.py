from django.contrib import admin
from learn_app.models import Kid,Student,Employee,UserProfile
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Kid)
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(UserProfile)
