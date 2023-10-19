from django.urls import path

from catalog.views import home_con, contacts_con


urlpatterns = [
    path('', home_con),
    path('contacts/', contacts_con),
]