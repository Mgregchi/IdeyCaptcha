from django.db import models

class Captcha(models.Model):
    INSTRUCTION_TYPE_CHOICES = [
        ('image', 'Image'),
        ('text', 'Text'),
    ]

    instruction = models.CharField(max_length=255)
    captcha_type = models.CharField(max_length=5, choices=INSTRUCTION_TYPE_CHOICES)

    def __str__(self):
        return self.instruction

class Option(models.Model):
    captcha = models.ForeignKey(Captcha, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.text if self.text else self.image_url
