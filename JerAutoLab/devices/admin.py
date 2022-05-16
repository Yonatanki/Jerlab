from django.contrib import admin

# Register your models here.
from .models import ADC, Router
# from .models import ADC

admin.site.register(ADC)
admin.site.register(Router)
# admin.site.register(Tag)