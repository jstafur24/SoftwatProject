from django.contrib import admin
from . models import Venta
# Register your models here.
# admin.site.register(Venta)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ["venta_id","price","amount","show_image1"]
    list_display_links = ["price", "amount"]
    # list_editable = ['amount']
    search_fields = ["amount"]
    list_filter = ["venta_id"]
    list_per_page = 5