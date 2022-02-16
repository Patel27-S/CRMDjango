from django.urls import path
from .views import lead_detail, lead_entry_form, lead_list


app_name = 'leads'

urlpatterns = [
    path('all/', lead_list),
    path('<int:pk>/', lead_detail),
    path('entryform/', lead_entry_form)
]