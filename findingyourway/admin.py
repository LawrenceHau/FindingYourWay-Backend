from django.contrib import admin
from .models import Adventure, Path, Route, Ending
# Register your models here.
admin.site.register(Adventure)
admin.site.register(Path)
admin.site.register(Route)
admin.site.register(Ending)

