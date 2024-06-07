from django.contrib import admin

# Register your models here.
from .models import Venue
from .models import MyClubUser
from .models import Event

admin.site.register(Venue)
admin.site.register(MyClubUser)
admin.site.register(Event)
