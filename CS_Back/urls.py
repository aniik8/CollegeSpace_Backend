from django.urls import path
from .views import *
urlpatterns = [
    path('view-notes', Notes_list),
    path('create-note', create_note),
    path(route='view-notes/<slug:slug>/<str:pk>', view=view_note),
    path('update-note/<slug:slug>/<str:pk>', update_note),
    path('delete-note/<slug:slug>/<str:pk>', delete_note),
    path('view-user-notes/<str:pk>', get_user_notes)
]
