from django.urls import path
from .views import index

app_name = "finance"

urlpatterns = [
    path('', index, name='index'),
]
