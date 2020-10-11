from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'title':'a title'})

def count(request):
    fulltext = request.GET['full-text']

    wordlist = fulltext.split()

    wordDict = {}

    for word in wordlist:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    sWords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'wordDict': sWords})

def about(request):
    return render(request, 'about.html')
