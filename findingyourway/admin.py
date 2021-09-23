from django.contrib import admin
from .models import Adventure, Path, RouteTableOne
# Register your models here.
admin.site.register(Adventure)
admin.site.register(Path)
admin.site.register(RouteTableOne)
