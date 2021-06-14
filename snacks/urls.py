from django.urls import path

from .views import snacksListView, snackDetailView

urlpatterns = [
    path('', snacksListView.as_view(), name="list"),
    path('<int:pk>/', snackDetailView.as_view(), name="details"),
]