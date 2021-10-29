from django.urls import path
from owner import views
urlpatterns=[
    path("numbertostring", views.Num_to_str, name="Numtostrconverter"),

]