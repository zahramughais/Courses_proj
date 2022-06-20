from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('newcourse', views.add_course),
    path('destroy/<int:id>', views.remove_course),
    path('delete/<int:id>', views.delete_course),
]