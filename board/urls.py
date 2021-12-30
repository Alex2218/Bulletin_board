from django.urls import path
from .views import info, by_rubric, BdCreateView


app_name = 'board'

urlpatterns = [
    path('add/', BdCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', info, name='info'),
]
