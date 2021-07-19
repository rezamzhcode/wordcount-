from django.http import HttpResponse
from django.shortcuts import render
import operator

def about(request):
    #about = request.GET['about']
    return render (request, 'about.html')
    

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    
    wordcountdictionary = {}
    for word in wordlist:
        if word in wordcountdictionary:
            #ncrease
            wordcountdictionary[word] += 1
        else:
                #add to dicitionary 
            wordcountdictionary[word] = 1

    sortedwords = sorted(wordcountdictionary.items(), key=operator.itemgetter(1),reverse=True)

        

    return render (request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist),'sortedwords':sortedwords})