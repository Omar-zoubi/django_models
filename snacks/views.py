from django.views.generic import ListView, DetailView
from .models import snacks

class snacksListView(ListView):
    template_name = "list.html"
    model = snacks

class snackDetailView(DetailView):
    template_name = "details.html"
    model = snacks
