from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import permissions

from .models import Content
from .serializers import ContentSerializer

# A view function, or view for short, is a Python function that takes a web request and returns a web response

class ContentView(APIView):
  """
  List all content entries or add, edit, delete one entry.
  """
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def get(self, request, format=None):
    content = Content.objects.all()
    serializer = ContentSerializer(content, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = ContentSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status.HTTP_201_CREATED)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

  def put(self, request, id, format=None):
    content = self.get_single_entry(id)
    serializer = ContentSerializer(content, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status.HTTP_201_CREATED)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

  def delete(self, request, id, format=None):
    content = self.get_single_entry(id)
    content.delete();
    return Response(status=status.HTTP_204_NO_CONTENT)

  def get_single_entry(self, id):
    try:
      return Content.objects.get(pk=id)
    except Content.DoesNotExist:
      raise Http404
