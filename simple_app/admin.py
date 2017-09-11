from django.contrib import admin
from simple_app.models import Event, Place, Schedule


admin.site.register(Event)
admin.site.register(Place)
admin.site.register(Schedule)