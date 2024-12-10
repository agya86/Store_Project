
from django.urls import path
from .views import StoreData

urlpatterns = [
    path('store/', StoreData.as_view()),
]
