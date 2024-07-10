from django.urls import path
from . import views

urlpatterns = [
    path("currencies/", views.CurrencyListCreate.as_view(), name="currency-list"),
]