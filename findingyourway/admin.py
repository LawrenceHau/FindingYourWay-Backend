from django.contrib import admin
from .models import Adventure, Path, RouteTableOne, RouteTableTwo, RouteTableThree, GoodEnding, BadEnding, NeutralEnding
# Register your models here.
admin.site.register(Adventure)
admin.site.register(Path)
admin.site.register(RouteTableOne)
admin.site.register(RouteTableTwo)
admin.site.register(RouteTableThree)
admin.site.register(GoodEnding)
admin.site.register(BadEnding)
admin.site.register(NeutralEnding)
