from django.urls import path
from .views import get_captcha, validate_captcha

urlpatterns = [
    path('get-captcha/', get_captcha, name='get_captcha'),
    path('validate-captcha/', validate_captcha, name='validate_captcha'),
]
