from django.urls import path
from pages import views

urlpatterns = [
    path('',  views.index, name="home"),
    path('about/',  views.about, name="about"),
    path('coc/',  views.code_of_conduct, name="code_of_conduct"),
]
