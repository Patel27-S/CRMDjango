from django.urls import path
from .views import lead_delete, lead_detail, lead_entry_form, lead_list, lead_update


app_name = 'leads'

urlpatterns = [
    path('all/', lead_list, name="lead_list"),
    path('<int:pk>/', lead_detail, name="lead_detail"),
    path('entryform/', lead_entry_form, name="lead_entry_form"),
    path('edit/<int:pk>',lead_update, name="lead_update"),
    path('delete/<int:something>', lead_delete, name="lead_delete")
]