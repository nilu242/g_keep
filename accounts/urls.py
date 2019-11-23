from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView
from .views import SignUpView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),

    path('change_pass/', PasswordChangeView.as_view(template_name="accounts/change_pass.html", success_url="/accounts/change_pass_done/"), name='change_pass'),
    path('change_pass_done/', PasswordChangeDoneView.as_view(template_name="accounts/change_pass_done.html"), name='password_change_done'),
]
