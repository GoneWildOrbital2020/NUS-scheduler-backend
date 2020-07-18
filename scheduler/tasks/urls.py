from django.urls import path
from .views import task, tasks

urlpatterns = [
    path('<str:name>/<int:id>', task),
    path('<str:name>', tasks),

]
