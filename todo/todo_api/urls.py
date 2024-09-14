from django.urls import path, include
from .views import (ToDoListApiView)

urlpatterns = [
    path('api', ToDoListApiView.as_view())
]