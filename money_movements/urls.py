from django.urls import path

from money_movements import views


urlpatterns = [
    path('money_movements', views.MoneyMovementsCreateListView.as_view())
]