from rest_framework import serializers
from .models import Captcha, Option

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'image_url']

class CaptchaSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Captcha
        fields = ['id', 'instruction', 'captcha_type', 'options']
