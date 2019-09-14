from celery import task
from django.http import HttpResponse

from deep_punc.models import Paragraph
from deep_punctuation.celery import app
from deepcorrect import DeepCorrect
from deepsegment import DeepSegment


@app.task
def processing(id):
    paragraph_object = Paragraph.objects.get(id=id)
    segmenter = DeepSegment('en')
    list_of_sentences = segmenter.segment(paragraph_object.original_text)
    corrector = DeepCorrect('deep_punc/deeppunct_params_en', 'deep_punc/deeppunct_checkpoint_wikipedia')
    # corrector = DeepCorrect('deeppunct_params_en', 'deeppunct_checkpoint_google_news')
    # corrector = DeepCorrect('deep_punc/deeppunct_params_en', 'deep_punc/deeppunct_checkpoint_tatoeba_cornell')
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

