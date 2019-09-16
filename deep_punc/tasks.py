from celery import task
from django.http import HttpResponse

from deep_punc.models import Paragraph
from deep_punctuation.celery import app
from deepcorrect import DeepCorrect
from deepsegment import DeepSegment
import threading
globals = threading.local()



@app.task
def processing(id):
    paragraph_object = Paragraph.objects.get(id=id)
    if not hasattr(globals, 'corrector') and not hasattr(globals, 'segmenter'):
        segmenter = DeepSegment('en')
        corrector = DeepCorrect('deep_punc/deeppunct_params_en', 'deep_punc/deeppunct_checkpoint_wikipedia')
        globals.corrector = corrector
        globals.segmenter = segmenter
    else:
        corrector = globals.corrector
        segmenter = globals.segmenter

    list_of_sentences = segmenter.segment(paragraph_object.original_text)
    paragraph = ''
    for i in range(len(list_of_sentences)):
        sentence = corrector.correct(list_of_sentences[i])
        if i == 0:
            paragraph += sentence[0]['sequence']
        else:
            paragraph += ' ' + sentence[0]['sequence']
    paragraph = paragraph.replace("\\", "")
    paragraph_object.processed_text = paragraph
    paragraph_object.processing=False
    paragraph_object.save()

