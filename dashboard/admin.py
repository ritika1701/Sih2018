from django.contrib import admin
from .models import SignUp, School,Academics, sports, Details, extra_curricular

# Register your models here.
admin.site.register(Details)
admin.site.register(SignUp)
admin.site.register(School)
admin.site.register(Academics)
admin.site.register(sports)
admin.site.register(extra_curricular)
