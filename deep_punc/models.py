from django.db import models

# Create your models here.


class Paragraph(models.Model):
    original_text = models.TextField()
    processed_text = models.TextField()
    processing = models.BooleanField(default=False)