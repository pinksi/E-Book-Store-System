"""mypart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'details.views.showcase', name ='showcase'),
    url(r'^sorted_showcase/(?P<choice_id>[0-9]+)$', 'details.views.sorted_showcase', name ='sorted_showcase'),
    url(r'^individual/(?P<book_id>[0-9]+)$', 'details.views.individual', name ='individual'),
    url(r'^category/(?P<category_id>[0-9]+)$', 'details.views.disp_category_wise', name ='category'),
    url(r'^recent/', 'details.views.recently_added', name ='recent'),
    url(r'^popular/', 'details.views.most_downloaded', name ='popular'),
    url(r'^booklist/', 'details.views.booklist', name ='booklist'),
    url(r'^aboutus/', 'details.views.about_us', name ='aboutus'),
    url(r'^admin/', admin.site.urls),
    url(r'^mycart/(?P<book_id>[0-9]+)$', 'cart.views.mycart', name='mycart'),
    url(r'^payment/(?P<cartbook_id>[0-9]+)$', 'cart.views.payment_option', name='payment_option'),
    url(r'^semifinal/(?P<payment_id>[0-9]+)/(?P<cartbook_id>[0-9]+)$', 'cart.views.semifinal', name='semifinal'),
    url(r'^final/(?P<payment_id>[0-9]+)/(?P<cartbook_id>[0-9]+)$', 'cart.views.final', name='final'),
    url(r'^mycart$', 'cart.views.mycart', name='mycart'),
    url(r'^accounts/', include('registration.backends.default.urls'))
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
