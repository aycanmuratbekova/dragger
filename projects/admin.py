from django.contrib import admin
from .models import Accessories


class AccessoriesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Accessories, AccessoriesAdmin)
