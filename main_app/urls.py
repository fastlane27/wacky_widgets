from django.urls import path
from . import views

urlpatterns = [
    path('', views.WidgetList.as_view(), name='index'),
    path('create/', views.create_widget, name='create_widget'),
    path('delete/<int:widget_id>/', views.delete_widget, name='delete_widget'),
]
