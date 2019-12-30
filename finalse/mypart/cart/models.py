from django.db import models
from details.models import Book
from django.utils import timezone

class Payment (models.Model):
	payment_option = models.CharField(max_length= 50)
	money_earned = models.FloatField(default=0.0)
	def __str__(self):
		return self.payment_option

class Cartbook (models.Model):
	
	m_book_name = models.CharField(max_length=30)
	m_user = models.CharField(max_length = 50, blank = True)
	m_author = models.CharField(max_length=30)
	m_price = models.FloatField(default = 0.0)
	purchased_bool = models.BooleanField(default = False)
	added_bookid = models.IntegerField(default = 0)
	date_added_to_cart = models.DateTimeField(auto_now_add=True, auto_now=False)
	date_purchased = models.DateTimeField(editable= True, blank = True)
	def __str__(self):
		return self.m_book_name



class Total (models.Model):
	total_money = models.FloatField(default=0.0)
	totaled_date = models.DateTimeField(editable= True, blank = True)
	def __str__(self):
		return str(self.total_money)