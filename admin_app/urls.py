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
    path('tables', views.tables, name='tables'),
    path('flot', views.flot, name='flot'),
    path('morris', views.morris, name='morris'),
    path('forms', views.forms, name='forms'),
    path('panels_wells', views.panels_wells, name='panels_wells'),
    path('buttons', views.buttons, name='buttons'),
    path('notifications', views.notifications, name='notifications'),
    path('typography', views.typography, name='typography'),
    path('icons', views.icons, name='icons'),
    path('grid', views.grid, name='grid'),
    path('blank', views.blank, name='blank'),
    path('login', views.login, name='login'),
    path('create', views.create, name='create'),
    path('network', views.network, name='network'),
    path('jabber', views.jabber, name='jabber'),
    path('email', views.email, name='email'),
  
]