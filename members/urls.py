from django.urls import path
from . import views


urlpatterns = [
    # 'login/ webpage url in browser
    #  views.login_user from views in members app
    path('login/', views.login_user, name="login"),
    
]