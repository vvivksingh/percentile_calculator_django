from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index, name='index'),
    # path('table',views.percentile_table, name='table')
]
