from django.shortcuts import render
from .models import Book
from .models import Category
from django.db.models import Q


def showcase(request):
	c = Category.objects.get(pk = 3)
	queryset1= c.book_set.all()[:6]
	c = Category.objects.get(pk = 1)
	queryset2= c.book_set.all()[:6]
	c = Category.objects.get(pk = 5)
	queryset3= c.book_set.all()[:6]
	all_books = Book.objects.all().order_by('-date_added')[:6]
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		context={
		'queryset1': queryset1,
		'queryset2': queryset2,
		'queryset3': queryset3,
		'all_books': all_books
		
	}
	return render(request, "showcase.html", context)
def search(request, query):
	queryset = Book.objects.order_by("book_name")
	queryset = queryset.filter(Q(book_name__icontains=query)|Q(author__icontains=query)).distinct()
	queryset = queryset.order_by("book_name")
			
	context = {
		'queryset': queryset
	}
	return render(request, "search.html", context)

def booklist(request):
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		booklist = Book.objects.all()
		context = {
			"booklist": booklist
		}
		return render(request, "booklist.html" , context)

def sorted_showcase(request, choice_id):
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		if int (choice_id) ==2:
			queryset = Book.objects.all().order_by('-price')
		elif int (choice_id) ==1:
			queryset = Book.objects.all().order_by('price')
		context={
			'booklist': queryset
		}
		return render(request, "booklist.html", context)


def disp_category_wise(request, category_id):
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		c = Category.objects.get(pk = category_id)		
		category_set= c.book_set.all()
		context={
			'category_set': category_set,
		}
		return render(request, "showcategory.html", context)

def individual (request, book_id):
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		b = Book.objects.get(pk = book_id)
		context = {
			'individual_set': b
		}

		return render(request, "individual.html", context)

def recently_added (request):
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		r = Book.objects.order_by('-date_added')[:3]
		context = {
			'recent_set':r
		}
		return render(request, "recent.html", context)

def most_downloaded (request):
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		c = Book.objects.order_by('-clicks')[:3]
		context = {
			'popular_clicks':c
		}
		return render(request, "popular.html", context)

def about_us(request):
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		a = Book.objects.order_by('book_name')
		context = {
			'about_us':a
		}
		return render(request,"aboutus.html",context)