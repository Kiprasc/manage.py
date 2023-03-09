from django.contrib import admin
from .models import Paslauga, Profilis, Product, Fencing, QuoteInstance, Hotel


class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')


class FencingAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')


class QuoteInstanceAdmin(admin.ModelAdmin):
    list_display = ('email', 'due_back', 'reader')
    list_filter = ('email', 'due_back')
    search_fields = ("email", "product__title")



admin.site.register(QuoteInstance, QuoteInstanceAdmin)
admin.site.register(Fencing, FencingAdmin)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Profilis)
admin.site.register(Hotel)