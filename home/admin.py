from django.contrib import admin

# Register your models here.
from home.models import *

admin.site.register(Contact)
admin.site.register(CollectResume)
admin.site.register(JobApply)
