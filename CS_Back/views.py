from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from django.utils.text import slugify
from .serializers import Notes_Serailzer
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['get'])
def Notes_list(request):
    notes = Notes.objects.all()
    notes_serializers = Notes_Serailzer(notes, many=True)
    return Response(notes_serializers.data)

@api_view(['get'])
def view_note(request, slug, pk):
    try:
        notes = Notes.objects.get(id=pk)
        notes_serializers = Notes_Serailzer(notes, many=False)
        return Response(notes_serializers.data)
    except:
        print("This portion is running ")
        return JsonResponse({'Message' : "Note Does not exist"})

@api_view(['get'])
def get_user_notes(request, pk):
    notes = Notes.objects.filter(user_id=pk)
    notes_Serailzer = Notes_Serailzer(notes, many=True)
    return Response(notes_Serailzer.data)
#create note~, view notes~, view single~, update~, delete~, 

@api_view(['post'])
def create_note(request):
    notes_serializer = Notes_Serailzer(data=request.data)
    if notes_serializer.is_valid():
        note_instance =  notes_serializer.save()
        note_instance.slug = slugify(note_instance.notes_title)
        note_instance.save()
        return Response(notes_serializer.data)
    return Response(notes_serializer.errors)

@api_view(['post'])
def update_note(request, slug, pk):
    try:
        note = Notes.objects.get(id=pk)
        notes_serializer = Notes_Serailzer(instance=note, data=request.data)
        if notes_serializer.is_valid():
            notes_instance = notes_serializer.save()
            notes_instance.slug = slugify(notes_instance.notes_title)
            notes_instance.save()
            return Response(notes_serializer.data)
        return Response(notes_serializer.errors)    
    except:
        return JsonResponse({'Message' : "Note Does not exist"})
        

@api_view(['delete'])
def delete_note(request, slug, pk):
    try:
        note = Notes.objects.get(id=pk)
        note.delete()
        return JsonResponse({
            'status' : 'Deleted'
        })
    except:
        return JsonResponse({'Message' : 'Note does not exist'})