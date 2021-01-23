from django.urls import path
from . import views

urlpatterns = [
  path('update_task/<str:primary_key>/',views.UpdateWork,name="update_task"),
 path('delete_task/<str:primary_key>/',views.delete_item,name="delete_task"),
  path('',views.index,name="indexx"),
]
