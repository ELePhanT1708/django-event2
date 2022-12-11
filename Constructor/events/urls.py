from django.urls import path
from .views import ViewPartners, ViewHome
urlpatterns = [
    path('', ViewHome.as_view(), name='home'),
    path('contact/', ViewPartners.as_view(), name='contact'),
    path('register/', ViewPartners.as_view(), name='register'),
    path('logout/', ViewPartners.as_view(), name='logout'),
    path('login/', ViewPartners.as_view(), name='login'),
    path('clients/<int:id_client>', ViewPartners.as_view(), name='clients'),
    path('partners/<int:id_partner>', ViewPartners.as_view(), name='partner'),
    path('partners/', ViewPartners.as_view(), name='partners'),

]