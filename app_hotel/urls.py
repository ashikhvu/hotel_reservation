from django.urls import path
from app_hotel import views

urlpatterns = [
    path('',views.home,name='home'),
    path('get_filtered_rooms',views.get_filtered_rooms,name='get_filtered_rooms'),
    path('book_reservation',views.book_reservation,name='book_reservation'),
    path('logout_admin',views.logout_admin,name='logout_admin'),
]