from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)


"""def removepunc(request):
    #print(request.GET.get('text','default'))
    djtext=request.GET.get('text','default')
    print(djtext)
    return HttpResponse("removepunc")

def capfirst(request):
    return HttpResponse("capitilize first")

def newlineremove(request):
    return HttpResponse("newlineremove")

def spaceremove(request):
    return HttpResponse("spaceremove <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("charcount")"""