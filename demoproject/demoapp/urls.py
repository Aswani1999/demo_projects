from  .import views
from django.urls import path

urlpatterns = [
    # path('',views.home,name="home"),
    # path('abouts/',views.abouts,name="abouts"),
    # path('contacts/',views.contacts,name="contacts"),
    # path('details/',views.details,name="details"),
    # path('thanks/',views.thanks,name="thanks")
    path('',views.demo,name="demo"),
    path('operation/',views.calculation,name="calculation")

]