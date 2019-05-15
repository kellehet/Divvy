from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dividends'),
    path('<int:symbol>', views.dividend, name='dividends'),

]
