from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('hotel_images', views.display_hotel_images, name = 'hotel_images'),
    path('userquotes/create', views.UserQuoteInstanceCreateView.as_view(), name='user_quoteinstance_create'),
    path('paslaugos/', views.PaslaugaListView.as_view(), name="paslaugos"),
    path('search/', views.search, name="search"),
    path("register/", views.register, name="register"),
    path("profilis/", views.profilis, name="profilis"),
    path('products/', views.ProductListView.as_view(), name="products"),
    path('fencings/', views.FencingListView.as_view(), name="fencings"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)