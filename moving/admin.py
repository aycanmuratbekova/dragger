from django.contrib import admin
from .models import Card, Category


class CardAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Card, CardAdmin)
admin.site.register(Category, CategoryAdmin)
