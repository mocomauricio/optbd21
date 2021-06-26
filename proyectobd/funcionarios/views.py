from django.utils import timezone
from django.views.generic.list import ListView

from .models import Marcacion

class MarcacionListView(ListView):
    model = Marcacion
    template_name = 'marcaciones.html'