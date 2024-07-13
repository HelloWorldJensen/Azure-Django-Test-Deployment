from django.urls import path
from . import views

urlpatterns = [
    path("holidays/", views.HolidayListCreate.as_view(), name="holiday-list"),
    path("currencies/", views.CurrencyListCreate.as_view(), name="currency-list"),
    path("exchanges/", views.ExchangeListCreate.as_view(), name="exchange-list"),    
    path("instruments/", views.InstrumentListCreate.as_view(), name="instrument-list"),    
    path("filter-categories/", views.FilterCategoryListCreate.as_view(), name="filter-category-list"),
    path("ordering-options/", views.OrderingOptionListCreate.as_view(), name="ordering-option-list"),
    path("view-options/", views.ViewOptionListCreate.as_view(), name="view-option-list"),
    path("saved-filters/", views.SavedFilterListCreate.as_view(), name="saved_filter-list"),
    path("trades/", views.TradeListCreate.as_view(), name="trade-list"),
    path("historical-positions/", views.HistoricalPositionListCreate.as_view(), name="historical-position-list"),
    path("historical-pls/", views.HistoricalPLListCreate.as_view(), name="historical-pl-list"),
    path("filter-results/", views.FilterResultListCreate.as_view(), name="filter-result-list"),
    path("filter-options/", views.FilterOptionListCreate.as_view(), name="filter-option-list"),
    path("close-prices/", views.ClosePriceListCreate.as_view(), name="close-price-list"),
]