from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Captcha, Option
from .serializers import CaptchaSerializer
import json

@api_view(['GET'])
def get_captcha(request):
    captcha = Captcha.objects.order_by('?').first()  # Fetch a random captcha
    serializer = CaptchaSerializer(captcha)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['POST'])
def validate_captcha(request):
    data = request.data
    user_selection = data.get('selection')
    captcha_id = data.get('captcha_id')
    captcha = Captcha.objects.get(id=captcha_id)
    correct_option = captcha.options.filter(text="correct_text").first()  # Update logic for correct option

    if correct_option and (user_selection == correct_option.text or user_selection == correct_option.image_url):
        return JsonResponse({'result': 'success'})
    else:
        return JsonResponse({'result': 'failure'})
