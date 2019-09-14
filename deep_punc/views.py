import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from deep_punc.models import Paragraph
from deep_punc.tasks import processing


def home(request):
    if request.method == 'GET':
        return render(request, 'base.html')


def submit_plain_text(request):
    if request.method == 'POST':
        rough_paragraph = request.POST.get('paragraph')
        paragraph_object = Paragraph.objects.create(original_text=rough_paragraph,
                                                    processed_text='',
                                                    processing=True)
        paragraph_object.save()
        paragraph_id = paragraph_object.id
        processing.delay(paragraph_id)
        context = {'original_text': rough_paragraph, 'paragraph_id': paragraph_id}
        return render(request, 'results.html', context)


def processing_text(request, id):
    if request.method == 'GET':
        paragraph = Paragraph.objects.filter(id=id).first()
        data = {"response": paragraph.processed_text, "processing": paragraph.processing}
        return JsonResponse(data)
