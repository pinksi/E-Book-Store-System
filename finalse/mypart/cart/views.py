from django.shortcuts import render
from .models import Cartbook
from .models import Payment
from .models import Total
from django.utils import timezone
from details.models import Book
from details.views import search

def mycart (request, book_id=0):
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		if book_id != 0:
			reference= 0	
			for instance in Cartbook.objects.all().filter(m_user__exact= request.user):
				if instance.added_bookid == int(book_id):
					reference = 1
					break
			if reference != 1 :
				b = Book.objects.get(pk = book_id)
				b.clicks= b.clicks + 1
				b.save()
				cb = Cartbook(m_book_name = b.book_name, m_author= b.author, m_price= b.price, m_user=request.user, added_bookid= book_id)		
				cb.save()
		print (request.user)	
		queryset = Cartbook.objects.all().order_by('-date_added_to_cart').filter(m_user__exact= request.user)
		context = {
			'queryset' : queryset
		}
		return render(request, "mycart.html", context)

def payment_option (request, cartbook_id):
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		b = Cartbook.objects.get(pk= cartbook_id)
		b.purchased_bool = True
		b.save()
		po = Payment.objects.all()
		context = {
			'queryset': po,
			'book_to_buy':b
		}

		return render(request, "payment_opt.html", context)

def semifinal(request, payment_id, cartbook_id):
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		p = Payment.objects.get(pk = payment_id)
		cb = Cartbook.objects.get(pk = cartbook_id)
		context={
			'chosen_option': p,
			'book_to_buy': cb
		}
		return render(request, "semifinal.html", context)

def final(request, payment_id, cartbook_id):
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		p = Payment.objects.get(pk = payment_id)
		cb = Cartbook.objects.get(pk = cartbook_id)
		cb.purchased_bool = True
		cb.date_purchased = timezone.now()
		print(cb.date_purchased)
		cb.save()
		payment_ko_sabai = Payment.objects.all()
		p.money_earned+= cb.m_price
		p.save()
		sum = 0
		for instance in payment_ko_sabai:
			sum += instance.money_earned
		tm = Total(total_money = sum, totaled_date = timezone.now()) 
		tm.save()
		context={
			'chosen_option': p,
			'book_to_buy': cb
		}
		return render(request, "final.html", context)


