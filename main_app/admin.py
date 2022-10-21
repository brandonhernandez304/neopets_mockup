from django.contrib import admin
from .models import Neopet, Toy, Feeding
# Register your models here.
admin.site.register(Neopet)
admin.site.register(Feeding)
admin.site.register(Toy)