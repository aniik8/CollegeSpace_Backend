from django.urls import path
from .views import *
urlpatterns = [
    path('questions', view_questions),
    path('question/<slug:slug>/<str:pk>', view_QA),
    path('create-question', create_question),
    path('create-answer', create_answer),
    path('update-question/<slug:slug>/<str:pk>', update_question),
    path('update-answer/<str:pk>', update_answer),
    path('delete-answer/<str:pk>', delete_answer),
    path('delete-question/<str:pk>', delete_question),
    path("view-answer/<str:pk>", getAnswer),

]
