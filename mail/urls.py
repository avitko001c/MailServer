from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('sendmail/', views.send_email, name="sendmail"),
    path('sent/', views.sent, name="sent"),
    path('password-change/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', email_template_name='password_reset_email.html', subject_template_name='password_reset_subject.txt',  success_url = reverse_lazy('user_accounts:password_reset_done')), name='password_reset'),
    path('password-change/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-change/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', success_url = reverse_lazy('user_accounts:password_reset_complete')), name='password_reset_confirm'),
    path('password-change/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete')
]
