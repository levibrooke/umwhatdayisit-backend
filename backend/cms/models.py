from django.db import models

class Content(models.Model):
  DAYOFWEEK_CHOICES = [
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday')
  ]

  dayOfWeek = models.CharField(max_length = 512, choices = DAYOFWEEK_CHOICES)

  MEDIATYPE_CHOICES = [
    ('image', 'image'),
    ('video', 'video'),
    ('twitter-embed', 'twitter-embed')
  ]
  mediaType = models.CharField(max_length=512, choices=MEDIATYPE_CHOICES)

  mediaLink = models.URLField()
  alt = models.CharField(max_length=512)
  message = models.TextField()

  def __str__(self):
    return self.alt
