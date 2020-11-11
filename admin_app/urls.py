from django.urls import path
from .views import (
    LogsListView,
    LogsDetailView,
    LogsCreateView,
    LogsUpdateView,
    LogsDeleteView


)
from . import views 

app_name = 'admin_app'
urlpatterns = [
    path('', LogsListView.as_view(), name='index'),
    path('logs/<int:pk>/', LogsDetailView.as_view(), name='logs-detail'),
    path('logs/new/', LogsCreateView.as_view(), name='logs-create'),
    path('logs/<int:pk>/update/', LogsUpdateView.as_view(), name='logs-update'),
    path('logs/<int:pk>/delete/', LogsDeleteView.as_view(), name='logs-delete'),
    path('network', views.network, name='network'),
    path('jabber', views.jabber, name='jabber'),
    path('email', views.email, name='email'),
  
]