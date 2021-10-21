from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/about/%Y/%m/%d/')
    description = RichTextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255, default='https://www.facebook.com/HiteshChoudharyPage')
    li_link = models.CharField(max_length=255, default='https://www.linkedin.com/in/hiteshchoudhary')
    ig_link = models.CharField(max_length=255, default='https://www.instagram.com/hiteshchoudharyofficial')
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    btn_text = models.CharField(max_length=255)
    btn_link = models.CharField(max_length=255, default='https://pro.learncodeonline.in/learn')
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

