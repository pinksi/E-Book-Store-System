from django.contrib import admin
from .models import Cartbook
from .models import Payment
from .models import Total

class CartbookAdmin(admin.ModelAdmin):
	list_display= ["m_user", "m_book_name", "m_author","m_price", "purchased_bool", "added_bookid"]

class PaymentAdmin(admin.ModelAdmin):
	list_display= ["payment_option", "money_earned"]

class TotalAdmin(admin.ModelAdmin):
	list_display= ["total_money", "totaled_date"]
	
admin.site.register(Cartbook, CartbookAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Total, TotalAdmin)
