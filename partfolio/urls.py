from django.urls import path
from partfolio.views import index

urlpatterns = [
  path('',  index, name="home")
]
