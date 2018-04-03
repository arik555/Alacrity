from django.contrib import admin
from .models import Event, MyGroup, MyUser
# Register your models here.
admin.site.register(Event)
admin.site.register(MyUser)
admin.site.register(MyGroup)