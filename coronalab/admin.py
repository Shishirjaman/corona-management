from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(RegUser)
admin.site.register(TestCenter)
admin.site.register(Test)
admin.site.register(WorldUpdate)
admin.site.register(BangladeshUpdate)
