from django.contrib import admin
from .models import Customer, Computer, Service, Booking

admin.site.register(Customer)
admin.site.register(Computer)
admin.site.register(Service)
admin.site.register(Booking)

