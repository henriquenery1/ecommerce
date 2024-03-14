from django.urls import path

from store.views.homepage import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
]
