from django.test import TestCase

# Create your tests here.
from django.utils import timezone
import datetime
from .models import Item

class ItemTest(TestCase):
	def test_was_purchased_this_month(self):
		"""
		was_purchased_this_month() should return false for items whose purchase_time is in the future
		"""
		time = timezone.now()+ datetime.timedelta(days=1)
		future_item = Item(purchase_time=time)
		self.assertIs(future_item.was_purchased_this_month(),False)