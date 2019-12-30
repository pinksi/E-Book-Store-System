from django.db import models

class Category (models.Model):
	category_head = models.CharField(max_length=20, default='None')
	def __str__(self):
		return self.category_head

class Book (models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	book_name = models.CharField(max_length=30)
	author = models.CharField(max_length=30)
	genre = models.CharField(max_length=40)
	price = models.FloatField(default = 0.0)
	date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
	pub_date = models.CharField(max_length=10)
	clicks = models.IntegerField(default=0)
	book_description = models.TextField()
	details = models.CharField(max_length=70)
	upload_image = models.ImageField(upload_to='uploads/', blank = True)
	#added_to_cart_bool = models.BooleanField(default = None)


	def __str__(self):
		return self.book_name
	

