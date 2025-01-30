from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.zapis_korisnika, name='record'),
    path('delete_record/<int:pk>', views.brisanje_zapisa, name='delete_record'),
    path('add_record/', views.dodavanje_zapisa, name='add_record'),
    path('update_record/<int:pk>', views.izmena_zapisa, name='update_record')
]
