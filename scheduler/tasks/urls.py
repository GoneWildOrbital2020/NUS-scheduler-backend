from django.urls import path
from .views import task, tasks

urlpatterns = [
    path('<str:username>/<str:name>/<int:id>', task),
    path('<str:username>/<str:name>', tasks),

]
