from django.urls import path

from .views import (
    apiOverview
)

app_name = 'api'
urlpatterns = [
    path('', apiOverview)
]
