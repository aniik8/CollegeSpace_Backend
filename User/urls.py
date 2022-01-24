from django.urls import path

from .views import *

urlpatterns = [
    path('register', CustomUserCreate.as_view()),
    path('logout/blacklist', BlacklistTokenUpdateView.as_view()),
    path('get_user/<str:pk>', getUser)
    # path("", userInfo)
]
