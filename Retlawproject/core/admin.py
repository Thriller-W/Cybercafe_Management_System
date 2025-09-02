from django.contrib import admin
from .models import Customer, Computer, Game, Booking, Payment
admin.site.register(Customer)
admin.site.register(Computer)
admin.site.register(Game)
admin.site.register(Booking)
admin.site.register(Payment)
