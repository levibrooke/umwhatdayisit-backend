from rest_framework import serializers
from cms.models import Content

class ContentSerializer(serializers.ModelSerializer):

  class Meta:
    model = Content
    fields = [
      'id',
      'dayOfWeek',
      'mediaType',
      'mediaLink',
      'alt',
      'message'
    ]
