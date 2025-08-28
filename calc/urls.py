from django.urls import path
from .  import views
urlpatterns = [
    path('',views.home,name='home'),
    path('numerical',views.numerical, name="numerical")
]
