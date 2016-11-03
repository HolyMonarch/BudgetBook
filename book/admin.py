from django.contrib import admin

# Register your models here.
from .models import Item

class ItemAdmin(admin.ModelAdmin):
	list_display = ('item_name', 'purchase_time', 'was_purchased_this_month')
	list_filter = ['purchase_time']
	fieldsets= [
		( None,        {'fields':['item_name','item_category']}),
		('Information',{'fields':['item_price','purchase_time','details']}),
	]

admin.site.register(Item, ItemAdmin)