from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

# Create your views here.
def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': lastest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# done part 3
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNoExist):
        #redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You didn\'t select a choice.'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return HttpResponseRedirect afert succesfully dealing
        # with POST data. This prevent data from being posted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))