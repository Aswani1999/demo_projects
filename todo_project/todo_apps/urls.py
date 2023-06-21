from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('',views.add,name="add"),
    path('detele/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('cbhome/',views.TaskListview.as_view(),name="cbhome"),
    path('cbdetails/<int:pk>/',views.TaskDetailView.as_view(),name="cbdetails"),
    path('cbupdate/<int:pk>/',views.Taskupdateview.as_view(),name="cbupdate"),
    path('cbdelete/<int:pk>/',views.TaskDeleteview.as_view(),name="cbdelete"),

 ]