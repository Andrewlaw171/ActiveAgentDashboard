from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Dashboard.as_view(), name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('draw-graph/', views.draw_graph, name='draw-graph'),
]