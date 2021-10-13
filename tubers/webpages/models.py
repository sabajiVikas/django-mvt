from django.db import models


class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    btn_text = models.CharField(max_length=255)
    btn_link = models.CharField(max_length=255, default='https://pro.learncodeonline.in/learn')
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

	