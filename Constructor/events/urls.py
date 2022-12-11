from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', HomeView.as_view(), name='contact'),
    path('register/', HomeView.as_view(), name='register'),
    path('logout/', HomeView.as_view(), name='logout'),
    path('login/', HomeView.as_view(), name='login'),
    path('clients/<int:id_client>', HomeView.as_view(), name='clients'),
    path('partners/<int:id_partner>', HomeView.as_view(), name='partners'),

]