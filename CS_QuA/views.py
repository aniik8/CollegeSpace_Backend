from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from django.utils.regex_helper import flatten_result
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from collections import namedtuple
from django.utils.text import slugify


# 1
@api_view(['get'])
def view_questions(request):
    questions = Question.objects.all()
    serializer = Question_serializer(questions, many=True)
    return Response(serializer.data)

@api_view(['post', 'get'])
def create_question(request):
    question_serializer = Question_serializer(data=request.data)
    if question_serializer.is_valid():
        question_instance = question_serializer.save()
        question_instance.slug = slugify(question_instance.question)
        question_instance.save()
        return Response(question_serializer.data)
    return Response(question_serializer.errors)

@api_view(['post'])
def update_question(request, slug, pk):
    question = Question.objects.get(id=pk)
    question_serializer = Question_serializer(instance=question, data=request.data)
    if question_serializer.is_valid():
        question_serializer.save()
        return Response(question_serializer.data)
    return Response(question_serializer.errors)

#3 view single qnA
"""used name tuple here by which we can make it into single tuple and can have its data"""
QnA = namedtuple('QnA', ('questions', 'answers'))
@api_view(['get'])
def view_QA(request, slug, pk):
    question = Question.objects.get(id=pk)
    answers = Answer.objects.filter(question_id=pk) #means we have those answers which have question_id as foreign key
    
    qna = QnA(Question_serializer(question, many=False).data, Answer_serializer(answers, many=True).data)
    return Response(qna)

@api_view(['post'])
def create_answer(request):
    answer_serializer = Answer_serializer(data=request.data)
    if answer_serializer.is_valid():
        answer_status = answer_serializer.save()
        
        answer_status.status = True
        answer_status.save()
        return Response(answer_serializer.data)
    return Response(answer_serializer.errors)
#https://stackoverflow.com/questions/52343062/updating-a-value-in-serializer-after-accessing-data-in-django-rest-framework
QnAns = namedtuple('QnAns', ('Answer', 'Question'))
@api_view(['post'])
def update_answer(request, pk):
    answer = Answer.objects.get(id=pk)
    question = Question.objects.get(id=answer.question.id)
    
    question_serializer = Question_serializer(question, many=False)
    answer_serializer = Answer_serializer(instance=answer, data=request.data)
    if answer_serializer.is_valid():
        answer_serializer.save()
        qNa = QnAns(answer_serializer.data, question_serializer.data)
        return Response(qNa)
    else:
        return JsonResponse(answer_serializer.errors)

#Decorator that converts a function-based view into an APIView subclass. 
# Takes a list of allowed methods for the view as an argument.
@api_view(['delete'])
def delete_answer(request, pk): 
    answer = Answer.objects.get(id=pk)
    answer.delete()
    return JsonResponse({'Response' : 'Deleted'})

@api_view(['delete'])
def delete_question(request, pk):
    question = Question.objects.get(id=pk)
    question.delete()
    return JsonResponse({'Response' : 'Deleted'})
#create update, delete , view -> question
#create update delete view -> answer

@api_view(['get'])
def getAnswer(request, pk):
    answer = Answer.objects.get(id=pk)
    answer_serializer = Answer_serializer(answer, many=False)
    return Response(answer_serializer.data)