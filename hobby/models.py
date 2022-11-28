from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=20)

class Hobby(models.Model):
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Hobby')
    title = models.CharField(max_length=80)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    tags = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    meeting_day = models.DateTimeField()
    address = models.CharField(max_length=100)
    X = models.CharField(max_length=30)
    Y = models.CharField(max_length=30)
    entry_fee = models.CharField(max_length=20)
    content = models.TextField()
    hits = models.PositiveBigIntegerField()
    recruit_type = models.BooleanField(default=False)
    limit = models.IntegerField(default=3, validators=[MinValueValidator(3), MaxValueValidator(15)])
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Accepted')
    image = models.ImageField(
        upload_to="images/",
        blank=True,
    )
    image_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 80},
    )

class Accepted(models.Model):
    joindate = models.DateTimeField(auto_now=True)
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    joined = models.BooleanField(default=False) # 승인여부

class Tag(models.Model):
    tag = models.CharField(max_length=20, unique=True)