from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    #print(fulltext) this print shows on command prompt
    wordlist = fulltext.split()

    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,"count.html",{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})




def display(request):
    enn_name = request.GET['enteredname']
    return render(request,'home.html',{'dis_name':enn_name})

def about(request):
    return render(request,'about.html')