from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SysUser
from .serializers import UserSerializer
from django.conf import settings
import os
from django.http import FileResponse, Http404

def generate_user_id():
    last_record = None
    try:
        last_record = SysUser.objects.last()
        print("this is lr", last_record)
        return "SIFRS_{}".format(last_record.id + 1)
    except:
        return "SIFRS_{}".format(1)


class RegisterUserView(APIView):
    parser_classes = [MultiPartParser, FormParser]


    def post(self, request):
        new_id = generate_user_id()
        print("NEW user id", new_id)
        request.data['user_id'] = new_id
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            image = request.data.get('user_image')
            if image:
                user.user_image = image
                user.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserView(APIView):
    def get(self, request, id):
        try:
            user = SysUser.objects.get(user_id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except SysUser.DoesNotExist:
            # If user is not found, return a 404 response
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)


class GetImageView(APIView):
    def get(self, request, image_name):
        image_path = None
        for ext in ['.jpg', '.jpeg', '.png', '.gif']:
            path = os.path.join(settings.BASE_DIR, 'images', image_name + ext)
            if os.path.isfile(path):
                image_path = path
                break
        if image_path is None:
            raise Http404
        return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')