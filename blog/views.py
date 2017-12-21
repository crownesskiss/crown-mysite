from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template  import loader

from django.views  import generic
from .models import Choice, Question
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'blog/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'blog/results.html'
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ',  '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('blog/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    return HttpResponse(output)
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blog/detail.html', {'question':question})
#结果显示页面
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blog/results.html', {'question': question})
    response = "you are looking result %s"
    return HttpResponse(response % question_id)
#投票系统

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'blog/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('blog:results', args=(question.id,)))
