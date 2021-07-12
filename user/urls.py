from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as as_view
from django.contrib.auth import views as auth_views 
from django.contrib.auth.forms import UserCreationForm
from user import views
from .models import Profile


urlpatterns = [
    path('login/', as_view.LoginView.as_view(template_name = "login.html"), name = "login"),
    path('logout/', as_view.LogoutView.as_view(), name = "logout"),
    path('register/' ,views.register , name="register" ),
    path('profile/', views.profile, name = "profile"),    
    path('update' , views.update_profile  ,name= "update_profile"),
    path('user/' , views.show_profile , name="show_profile"), 
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'), 
        name='password_change_form'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), 
        name='password_change_done'),
    path('password_reset',auth_views.PasswordResetView.as_view(template_name ='registeration/password_reset_form.html'), name = "password_reset_form"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name ='registeration/password_reset_done.html'), name= 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name ='registeration/password_reset_confirm.html'), name="password_reset_confirm"), 
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name ='registeration/password_reset_complete.html'), name='password_reset_complete')
] 
     


