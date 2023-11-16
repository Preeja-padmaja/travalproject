from. import views
from django .urls import path
urlpatterns = [
    path('', views.traval_fun,name='traval_fun'),
    path('register/',views.register_fun,name='register_fun'),
    path('login/',views.login_fun,name='login_fun'),
    path('logout/',views.logout_fun,name='logout_fun'),
]