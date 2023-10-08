
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('ucf/',views.usercform, name = 'registration'),
    path('login/',views.login_form, name = 'login'),
    path('success/',views.slogin,),
    path('logout/',views.logout_form, name = 'logout'),
]
