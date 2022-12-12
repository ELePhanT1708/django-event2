from django.urls import path
from .views import ViewPartners, ViewHome, register, user_logout
urlpatterns = [
    path('', ViewHome.as_view(), name='home'),
    path('contact/', ViewPartners.as_view(), name='contact'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('login/', ViewPartners.as_view(), name='login'),
    path('clients/<int:id_client>', ViewPartners.as_view(), name='clients'),
    path('vendors/profile/<int:id_partner>', ViewPartners.as_view(), name='vendor'),
    path('vendors/', ViewPartners.as_view(), name='vendors'),

]