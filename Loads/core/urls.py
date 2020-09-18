from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.terminal_login, name="terminal_login"),
    path('verify/<str:that_id>', views.terminal_verify, name="terminal_verify"),
    path('VRTS/<str:that_id>/<str:that_pass>',views.terminal_access,name="terminal_access"),
]