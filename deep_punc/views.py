from django.shortcuts import render
from deep_punc.tasks import processing
from celery.result import AsyncResult


def home(request):
    if request.method == 'GET':
        return render(request, 'base.html')


def submit_plain_text(request):
    if request.method == 'POST':
        rough_paragraph = request.POST.get('paragraph')
        print(rough_paragraph)
        punctuated_paragraph = processing.delay(rough_paragraph)
        res = AsyncResult(punctuated_paragraph.id)
        print(res)
        context = {'paragraph': punctuated_paragraph}
        return render(request, 'results.html', context)