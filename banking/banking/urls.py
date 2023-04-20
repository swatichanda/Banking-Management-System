from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/',views.about,name='about'),
    path('customers/', views.view_customers, name='view_customers'),
    path('customers/<int:pk>/', views.view_customer, name='view_customer'),
    path('transfer/', views.transfer, name='transfer')
]
