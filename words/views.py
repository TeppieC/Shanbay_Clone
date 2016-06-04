from django.shortcuts import render
from django.http import HttpResponse
from words.models import Word
from datetime import datetime


# Create your views here.
def home(request):
    word_list = Word.objects.all()
    return render(request, 'home.html', {'word_list': word_list})



def detail(request, my_args):
    word = Word.objects.all()[int(my_args)]
    mystr = ("text = %s, desc = %s, sentence = %s" % (word.text, word.desc, word.sentence))
    return HttpResponse(mystr)


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})
