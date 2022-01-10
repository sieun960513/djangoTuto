from django.http import HttpResponse, Http404

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.template import loader

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)
    # render 함수는 (requtest, 템플릿 이름, 선택적 인수, context로 httpResponse 반환됨)


def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)

    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "you're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("you're voting on question %s" % question_id)
