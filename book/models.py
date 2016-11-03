from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
	item_name=models.CharField(max_length=30)
	Category = (
		('R','Restaurants'),
		('S','Supermarksts'),
		('M','Merchandise/Retail'),
		('G','Gasoline'),
		('H','Home Improvement'),
		('O','Other')
		)
	item_category=models.CharField(max_length=1,choices=Category)
	item_price = models.IntegerField(default = 0)
	purchase_time = models.DateField('date')
	details = models.CharField(max_length=200)

	def __str__(self):
		return self.item_name

	def was_purchased_this_month(self):
		return self.purchase_time.month == timezone.now().month # and self.purchase_time < timezone.now()
	was_purchased_this_month.admin_order_field = 'purchase_time'
	was_purchased_this_month.boolean = True
	was_purchased_this_month.short_description = 'Purchased Recently?'