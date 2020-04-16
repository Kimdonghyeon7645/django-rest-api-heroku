from rest_framework import response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random


# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return response.Response("haha! I'm API from django rest framework")

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True)
    # many=True 옵션을 넣으면 다수의 데이터도 직렬화 진행 
    return response.Response(serializer.data)

