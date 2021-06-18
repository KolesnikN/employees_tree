from django.urls import path
from .views import *


urlpatterns = [
    path('', emp_tree),
    path('not_authenticated/', not_authenticated, name='not_authenticated_url'),
    path('tree/', emp_tree, name='emp_tree_url'),
    path('ajaxtree', ajax_tree),
]
