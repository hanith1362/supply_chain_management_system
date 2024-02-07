from django.contrib import admin
from supply_chain.models import seller_data1
class seller_dataAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','phone_number','email','shopname','gst_number','category','subcategory','product_number','product_price')
admin.site.register(seller_data1,seller_dataAdmin)
