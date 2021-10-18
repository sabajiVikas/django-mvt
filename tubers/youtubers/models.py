from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Youtuber(models.Model):

    crew_choices = (
        ('solo','solo'),
        ('small','small'),
        ('large','large'),
    )

    camera_choices = (
        ('canon', 'canon'),
        ('nikon', 'nikon'),
        ('sony', 'sony'),
        ('red', 'red'),
        ('fuji', 'fuji'),
        ('panasonic', 'panasonic'),
        ('others', 'others'),
    )

    category_choices = (
        ('code', 'code'),
        ('programming', 'programming'),
        ('vlogs', 'vlogs'),
        ('cooking', 'cooking'),
        ('animation', 'animation'),
    )

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="media/ytubers/%Y/%m/")
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(max_length=255, choices=crew_choices)
    camera_type = models.CharField(max_length=255, choices=camera_choices)
    subs_count = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=category_choices)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
