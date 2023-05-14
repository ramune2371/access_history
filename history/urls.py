from django.urls import path
from history.list_page import ListPage

urlpatterns = [
    path('', ListPage.list , name="list"),
]