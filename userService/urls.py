from django.urls import path
from userService.views import RegisterUserView, GetUserView, GetImageView

urlpatterns = [
    path('register', RegisterUserView.as_view()),
    path('get/<str:id>', GetUserView.as_view()),
    path('get_image/<str:image_name>', GetImageView.as_view()),

]
