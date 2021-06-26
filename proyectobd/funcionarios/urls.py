from django.urls import path

from .views import MarcacionListView

urlpatterns = [
    path('', MarcacionListView.as_view(), name='marcaciones_list')
]